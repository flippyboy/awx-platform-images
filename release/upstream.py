#!/usr/bin/env python3
"""Development-branch pin policy for awx-platform-images.

Stable semver tags (awx 24.6.x, ansible-ui v2.4.x) lag the branches where new
features land by years. Pins track ``devel`` (or ``main`` / ``master``) and,
for public images, the registry digest of the floating development tag.
"""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request

_RELEASE_TAG = re.compile(r"^v?\d+\.\d+(\.\d+)?([-+].+)?$")
_FULL_SHA = re.compile(r"^[0-9a-fA-F]{40}$")
_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
_COMPONENT_KEY = re.compile(r"^  [A-Za-z0-9][\w.-]*:\s*(?:#.*)?$")

# Git refs that are not where features land. ``latest`` is a floating image
# tag for Jewel, not a git branch we should pin.
GIT_SKIP = {"stable", "latest", "head", "release"}
DEV_BRANCHES = ("devel", "main", "master")
PIN_FIELDS = ("ref", "commit", "public_image", "public_image_digest")

USER_AGENT = "awx-platform-images-propose-pins"
MANIFEST_ACCEPT = ", ".join(
    [
        "application/vnd.oci.image.index.v1+json",
        "application/vnd.docker.distribution.manifest.list.v2+json",
        "application/vnd.docker.distribution.manifest.v2+json",
        "application/vnd.oci.image.manifest.v1+json",
    ]
)


def is_release_tag(ref: str) -> bool:
    return bool(_RELEASE_TAG.match((ref or "").strip()))


def is_full_sha(ref: str) -> bool:
    return bool(_FULL_SHA.fullmatch((ref or "").strip()))


def is_digest(value: str) -> bool:
    return bool(_DIGEST.fullmatch((value or "").strip()))


def tracking_ref_candidates(configured: str | None) -> list[str]:
    """Branch names to try, development branch first.

    A configured semver tag, ``stable``, ``latest``, or a raw commit is not a
    tracking branch. ``devel`` is preferred, then ``main``, then ``master``.
    """
    ref = (configured or "").strip()
    ordered: list[str] = []
    if ref and not is_release_tag(ref) and ref.lower() not in GIT_SKIP and not is_full_sha(ref):
        ordered.append(ref)
    for name in DEV_BRANCHES:
        if name not in ordered:
            ordered.append(name)
    return ordered


def image_tag_candidates(tag: str | None) -> tuple[list[str], str | None]:
    """Floating tags to resolve, plus the stable tag that was ignored.

    ``latest`` stays first when it is the configured tag (Jewel publishes the
    development line as ``latest`` and has no ``:devel`` image).
    """
    tag = (tag or "").strip()
    if not tag or is_release_tag(tag) or tag.lower() in {"stable", "release"}:
        return ["devel", "main", "latest"], (tag or None)
    ordered = [tag]
    for extra in ("devel", "main", "latest"):
        if extra not in ordered:
            ordered.append(extra)
    return ordered, None


def parse_github_repo(repo_url: str) -> tuple[str, str]:
    match = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", repo_url or "")
    if not match:
        raise ValueError(f"Not a GitHub URL: {repo_url}")
    return match.group(1), match.group(2)


def split_image(ref: str) -> tuple[str, str | None, str | None]:
    """Return ``(name, tag, digest)`` for ``ghcr.io/org/img:tag@sha256:...``."""
    body = (ref or "").strip()
    digest = None
    if "@" in body:
        body, digest = body.rsplit("@", 1)
        digest = digest or None
    tag = None
    last = body.split("/")[-1] if body else ""
    if ":" in last:
        body, tag = body.rsplit(":", 1)
        tag = tag or None
    return body, tag, digest


def pinned_image_ref(public_image: str, digest: str | None) -> str:
    """Image reference for a build. Digest wins over a floating tag."""
    name, tag, existing = split_image(public_image or "")
    chosen = (digest or "").strip() or (existing or "")
    if chosen and not is_digest(chosen):
        chosen = existing if existing and is_digest(existing) else ""
    if name and tag and chosen:
        return f"{name}:{tag}@{chosen}"
    if name and chosen:
        return f"{name}@{chosen}"
    if name and tag:
        return f"{name}:{tag}"
    return public_image or ""


def git_changed(old: dict, new: dict) -> bool:
    return (old.get("commit") or "").strip() != (new.get("commit") or "").strip() or (
        (old.get("ref") or "").strip() != (new.get("ref") or "").strip()
    )


def image_changed(old: dict, new: dict) -> bool:
    return (old.get("public_image") or "").strip() != (
        new.get("public_image") or ""
    ).strip() or (old.get("public_image_digest") or "").strip() != (
        new.get("public_image_digest") or ""
    ).strip()


def github_api(url: str, token: str | None) -> dict | list:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", USER_AGENT)
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")[:300]
        raise RuntimeError(f"GitHub {exc.code} for {url}: {body}") from exc


def resolve_commit(owner: str, repo: str, ref: str, token: str | None) -> str:
    quoted = urllib.parse.quote(ref, safe="")
    data = github_api(
        f"https://api.github.com/repos/{owner}/{repo}/commits/{quoted}",
        token,
    )
    if isinstance(data, dict) and data.get("sha"):
        return str(data["sha"])
    raise RuntimeError(f"Could not resolve {owner}/{repo}@{ref}")


def select_tracking_ref(
    owner: str, repo: str, configured: str | None, token: str | None
) -> tuple[str, str]:
    """Return ``(branch, tip_sha)`` for the development branch. Never a release tag."""
    errors: list[str] = []
    for candidate in tracking_ref_candidates(configured):
        try:
            return candidate, resolve_commit(owner, repo, candidate, token)
        except Exception as exc:
            errors.append(f"{candidate}: {exc}")
    detail = "; ".join(errors) if errors else "no branch candidates"
    raise RuntimeError(f"Could not resolve a development branch for {owner}/{repo} ({detail})")


def normalize_commit(item: dict) -> dict:
    commit = item.get("commit") or {}
    message = (commit.get("message") or "").replace("\r\n", "\n").strip()
    subject = message.splitlines()[0].strip() if message else "(no subject)"
    subject = subject.replace("`", "'")
    if len(subject) > 160:
        subject = subject[:157] + "..."
    date = (((commit.get("author") or {}).get("date")) or "")[:10]
    return {"sha": item.get("sha") or "", "date": date, "subject": subject}


def _walk_commits(
    owner: str,
    repo: str,
    base: str,
    head: str,
    token: str | None,
    cap: int,
) -> tuple[list[dict], bool]:
    """Newest-first walk of ``head`` until ``base`` or ``cap``. Returns oldest-first."""
    collected: list[dict] = []
    reached = False
    page = 1
    while len(collected) < cap and page <= 15:
        quoted = urllib.parse.quote(head, safe="")
        batch = github_api(
            f"https://api.github.com/repos/{owner}/{repo}/commits"
            f"?sha={quoted}&per_page=100&page={page}",
            token,
        )
        if not isinstance(batch, list):
            raise RuntimeError(f"unexpected commits payload for {owner}/{repo}")
        if not batch:
            break
        for item in batch:
            sha = str(item.get("sha") or "")
            if base and (sha == base or (len(base) >= 7 and sha.startswith(base))):
                reached = True
                break
            collected.append(normalize_commit(item))
            if len(collected) >= cap:
                break
        if reached or len(batch) < 100 or len(collected) >= cap:
            break
        page += 1
    collected.reverse()
    return collected, reached


def commits_since(
    owner: str,
    repo: str,
    base: str,
    head: str,
    token: str | None,
    limit: int = 150,
) -> dict:
    """Commits on ``head`` after ``base``, oldest first.

    Uses the compare API when both sides are commits so the list is the real
    range. A pin left on an old stable tag can be thousands of commits behind
    ``devel``; in that case the notes keep the newest ``limit`` commits, which
    is what a release note needs, and point at the compare link for the rest.
    """
    base = (base or "").strip()
    head = (head or "").strip()
    if base and head and base == head:
        return {
            "commits": [],
            "truncated": False,
            "reached_base": True,
            "no_base": False,
            "error": None,
        }

    no_base = not base
    if not no_base:
        base_q = urllib.parse.quote(base, safe="")
        head_q = urllib.parse.quote(head, safe="")
        try:
            data = github_api(
                f"https://api.github.com/repos/{owner}/{repo}/compare/{base_q}...{head_q}",
                token,
            )
        except Exception:
            data = None
        if isinstance(data, dict) and isinstance(data.get("commits"), list):
            commits = [normalize_commit(item) for item in data["commits"]]
            total = int(data.get("total_commits") or len(commits))
            if total <= len(commits) and len(commits) <= limit:
                return {
                    "commits": commits,
                    "truncated": False,
                    "reached_base": True,
                    "no_base": False,
                    "error": None,
                }
            # Compare truncated (GitHub caps the payload) or the range is too
            # long for notes. Keep the newest commits on the branch tip.
            newest, reached = _walk_commits(owner, repo, base, head, token, limit)
            return {
                "commits": newest,
                "truncated": True,
                "reached_base": reached,
                "no_base": False,
                "error": None,
            }

    cap = 40 if no_base else limit
    collected, reached = _walk_commits(owner, repo, base, head, token, cap)
    truncated = len(collected) >= cap if no_base else not reached
    return {
        "commits": collected,
        "truncated": truncated,
        "reached_base": reached,
        "no_base": no_base,
        "error": None,
    }


def format_commit_log(
    name: str,
    branch: str,
    old: str,
    new: str,
    info: dict,
    repo: str,
) -> list[str]:
    """Markdown changelog for one upstream. ``repo`` is ``owner/name``."""
    lines = [f"### `{name}` (`{branch}`)", ""]
    if info.get("error"):
        lines += [f"Could not list upstream commits: {info['error']}", ""]
        return lines
    if info.get("skipped"):
        shown = (new or old or "")[:12] or "—"
        lines += [f"Unchanged at `{shown}`.", ""]
        return lines

    commits = info.get("commits") or []
    compare = ""
    if repo and len(old) >= 7 and len(new) >= 7:
        compare = f" [compare](https://github.com/{repo}/compare/{old}...{new})"
    if not commits:
        lines += [f"No new upstream commits.{compare}", ""]
        return lines

    if info.get("no_base"):
        extra = " No previous commit; showing the latest commits on the development branch."
    elif info.get("truncated") and not info.get("reached_base"):
        extra = (
            " Previous pin is outside this window; showing the latest"
            " development-branch commits."
        )
    elif info.get("truncated"):
        extra = " List truncated."
    else:
        extra = ""
    old_s = old[:12] if old else "none"
    lines += [
        f"`{old_s}` → `{new[:12]}` — {len(commits)} commits.{extra}{compare}",
        "",
    ]
    for commit in commits:
        sha = commit.get("sha") or ""
        short = sha[:12]
        if repo and sha:
            shown = f"[`{short}`](https://github.com/{repo}/commit/{sha})"
        else:
            shown = f"`{short}`"
        date = commit.get("date") or ""
        subject = commit.get("subject") or ""
        lines.append(f"- {shown} {date} {subject}".rstrip())
    lines.append("")
    return lines


def _registry_token(repository: str) -> str:
    url = f"https://ghcr.io/token?service=ghcr.io&scope=repository:{repository}:pull"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", USER_AGENT)
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.loads(resp.read().decode())
    token = payload.get("token") or payload.get("access_token")
    if not token:
        raise RuntimeError(f"no registry token for {repository}")
    return str(token)


def manifest_digest(image_name: str, tag: str) -> str:
    if not image_name.startswith("ghcr.io/"):
        raise RuntimeError(f"only ghcr.io images are resolved, got {image_name}")
    repository = image_name[len("ghcr.io/") :]
    token = _registry_token(repository)
    quoted = urllib.parse.quote(tag, safe="")
    req = urllib.request.Request(
        f"https://ghcr.io/v2/{repository}/manifests/{quoted}",
        method="GET",
    )
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", MANIFEST_ACCEPT)
    req.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            digest = resp.headers.get("Docker-Content-Digest") or ""
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"{image_name}:{tag} HTTP {exc.code}") from exc
    if not is_digest(digest):
        raise RuntimeError(f"no digest for {image_name}:{tag}")
    return digest


def suggest_public_image(public_image: str) -> dict:
    """Digest of the development image. Stable version tags are not used."""
    name, tag, _digest = split_image(public_image)
    if not name:
        return {
            "image": "",
            "tag": None,
            "digest": None,
            "ignored_tag": None,
            "error": "empty public_image",
        }
    candidates, ignored = image_tag_candidates(tag)
    errors: list[str] = []
    for candidate in candidates:
        try:
            return {
                "image": name,
                "tag": candidate,
                "digest": manifest_digest(name, candidate),
                "ignored_tag": ignored,
                "error": None,
            }
        except Exception as exc:
            errors.append(f"{candidate}: {exc}")
    return {
        "image": name,
        "tag": None,
        "digest": None,
        "ignored_tag": ignored,
        "error": "; ".join(errors) if errors else "no tag",
    }


def _find_component_span(lines: list[str], name: str) -> tuple[int, int] | None:
    comp_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^components:\s*$", line.rstrip("\n")):
            comp_idx = i
            break
    if comp_idx is None:
        return None
    key_re = re.compile(rf"^  {re.escape(name)}:\s*(?:#.*)?$")
    start = None
    for i in range(comp_idx + 1, len(lines)):
        raw = lines[i].rstrip("\n")
        if start is None:
            if key_re.match(raw):
                start = i + 1
            elif raw.strip() and not lines[i].startswith((" ", "#")):
                return None
            continue
        if _COMPONENT_KEY.match(raw):
            return start, i
        if raw.strip() and not lines[i].startswith((" ", "#")):
            return start, i
    if start is None:
        return None
    return start, len(lines)


def _detect_indent(lines: list[str], start: int, end: int) -> str:
    for i in range(start, end):
        stripped = lines[i].lstrip(" ")
        if stripped and not stripped.startswith("#"):
            return lines[i][: len(lines[i]) - len(stripped)]
    return "    "


def _parse_scalar_rest(rest: str) -> tuple[str, str]:
    """Split the text after ``key:`` into ``(value, trailing comment)``."""
    s = rest.lstrip(" ")
    if s.startswith('"'):
        i = 1
        while i < len(s):
            if s[i] == "\\":
                i += 2
                continue
            if s[i] == '"':
                value = s[1:i].replace('\\"', '"').replace("\\\\", "\\")
                return value, s[i + 1 :]
            i += 1
        return s.strip('"'), ""
    if s.startswith("'"):
        end = s.find("'", 1)
        if end != -1:
            return s[1:end], s[end + 1 :]
    if " #" in s:
        value, comment = s.split(" #", 1)
        return value.strip(), " #" + comment
    return s.strip(), ""


def _format_scalar(key: str, value: str) -> str:
    # Digests contain a colon. Quote them so they stay one scalar.
    if key == "public_image_digest":
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if value and value.lower() not in {"true", "false", "null", "yes", "no"}:
        if not re.search(r"[\s#\"'\[\]{}|>&*!?,]", value) and not (
            ": " in value or value.endswith(":")
        ):
            return value
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _format_field_line(indent: str, key: str, value: str, comment: str) -> str:
    suffix = comment or ""
    if suffix and not suffix.startswith(" ") and not suffix.startswith("\n"):
        suffix = " " + suffix
    return f"{indent}{key}: {_format_scalar(key, value)}{suffix}\n"


def _apply_fields(
    lines: list[str], start: int, end: int, fields: dict[str, str]
) -> tuple[int, bool]:
    indent = _detect_indent(lines, start, end)
    changed = False
    for key, value in fields.items():
        if key not in PIN_FIELDS:
            raise ValueError(f"refusing to edit pin field {key}")
        found = None
        prefix = f"{indent}{key}:"
        for i in range(start, end):
            raw = lines[i].rstrip("\n")
            if raw.startswith(prefix):
                found = i
                break
        if found is None:
            anchor = {
                "public_image_digest": "public_image",
                "commit": "ref",
            }.get(key)
            insert_at = start
            if anchor:
                anchor_prefix = f"{indent}{anchor}:"
                for i in range(start, end):
                    if lines[i].rstrip("\n").startswith(anchor_prefix):
                        insert_at = i + 1
                        break
            lines.insert(insert_at, _format_field_line(indent, key, value, ""))
            end += 1
            changed = True
            continue
        raw = lines[found].rstrip("\n")
        current, comment = _parse_scalar_rest(raw[len(prefix) :])
        newline = "\n" if lines[found].endswith("\n") else ""
        if current == value:
            continue
        lines[found] = _format_field_line(indent, key, value, comment).rstrip("\n") + newline
        changed = True
    return end, changed


def _replace_updated(text: str, updated: str) -> str:
    def repl(match: re.Match[str]) -> str:
        return f'{match.group(1)}"{updated}"'

    new, count = re.subn(
        r'^(updated:\s*)(?:"[^"]*"|\'[^\']*\'|\S+)',
        repl,
        text,
        count=1,
        flags=re.M,
    )
    return new if count else text


def apply_pin_updates(
    text: str,
    updates: dict[str, dict[str, str]],
    updated: str | None = None,
) -> tuple[str, bool]:
    """Edit pin scalars in ``text`` and keep comments and key order.

    ``updates`` maps a component name to fields (``ref``, ``commit``,
    ``public_image``, ``public_image_digest``). ``updated`` is written only
    when a pin field actually changes.
    """
    lines = text.splitlines(keepends=True)
    changed = False
    for name, fields in updates.items():
        span = _find_component_span(lines, name)
        if span is None:
            raise ValueError(f"component {name!r} not found under components:")
        start, end = span
        end, did = _apply_fields(lines, start, end, fields)
        changed = changed or did
    new = "".join(lines)
    if changed and updated:
        new = _replace_updated(new, updated)
    return new, changed
