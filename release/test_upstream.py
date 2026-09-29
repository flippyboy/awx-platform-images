#!/usr/bin/env python3
"""Policy tests: pins track devel/main, never a stable upstream tag."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import yaml

import upstream

ROOT = Path(__file__).resolve().parents[1]


def _load_render_notes():
    path = Path(__file__).resolve().parent / "render-notes.py"
    spec = importlib.util.spec_from_file_location("render_notes", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


render_notes = _load_render_notes()


class TrackingRefTest(unittest.TestCase):
    def test_release_tags(self):
        for ref in ("24.6.1", "v2.4.313", "v2.4.313-rc.1", "1.2"):
            self.assertTrue(upstream.is_release_tag(ref), ref)
        for ref in ("devel", "main", "master", "latest", "stable", "feature"):
            self.assertFalse(upstream.is_release_tag(ref), ref)

    def test_stable_tag_is_not_a_tracking_branch(self):
        self.assertEqual(
            upstream.tracking_ref_candidates("24.6.1"),
            ["devel", "main", "master"],
        )
        self.assertEqual(
            upstream.tracking_ref_candidates("v2.4.313"),
            ["devel", "main", "master"],
        )
        self.assertEqual(
            upstream.tracking_ref_candidates("stable"),
            ["devel", "main", "master"],
        )
        self.assertEqual(
            upstream.tracking_ref_candidates("a" * 40),
            ["devel", "main", "master"],
        )

    def test_configured_development_branch_stays_first(self):
        self.assertEqual(
            upstream.tracking_ref_candidates("devel"),
            ["devel", "main", "master"],
        )
        self.assertEqual(
            upstream.tracking_ref_candidates("main"),
            ["main", "devel", "master"],
        )

    def test_image_tags_skip_stable_versions(self):
        self.assertEqual(
            upstream.image_tag_candidates("24.6.1"),
            (["devel", "main", "latest"], "24.6.1"),
        )
        self.assertEqual(
            upstream.image_tag_candidates("v2.4.313"),
            (["devel", "main", "latest"], "v2.4.313"),
        )
        self.assertEqual(
            upstream.image_tag_candidates("stable"),
            (["devel", "main", "latest"], "stable"),
        )

    def test_jewel_latest_stays_the_development_tag(self):
        # Jewel publishes the devel line as :latest and has no :devel image.
        self.assertEqual(
            upstream.image_tag_candidates("latest"),
            (["latest", "devel", "main"], None),
        )
        self.assertEqual(
            upstream.image_tag_candidates("devel"),
            (["devel", "main", "latest"], None),
        )


class PinnedImageTest(unittest.TestCase):
    def test_digest_pins_the_floating_tag(self):
        digest = "sha256:" + "ab" * 32
        self.assertEqual(
            upstream.pinned_image_ref("ghcr.io/ansible/awx:devel", digest),
            f"ghcr.io/ansible/awx:devel@{digest}",
        )

    def test_missing_digest_keeps_the_tag(self):
        self.assertEqual(
            upstream.pinned_image_ref("ghcr.io/ansible/jewel:latest", None),
            "ghcr.io/ansible/jewel:latest",
        )
        self.assertEqual(
            upstream.pinned_image_ref("ghcr.io/ansible/jewel:latest", "not-a-digest"),
            "ghcr.io/ansible/jewel:latest",
        )


class ApplyPinUpdatesTest(unittest.TestCase):
    def test_real_pins_keep_comments_and_other_components(self):
        text = (ROOT / "pins.yaml").read_text(encoding="utf-8")
        loaded_before = yaml.safe_load(text)
        old_awx = loaded_before["components"]["awx"]["commit"]
        old_jewel = loaded_before["components"]["jewel"]["commit"]
        digest = "sha256:" + "ab" * 32
        new_commit = "e995e5fc5f92aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        new, changed = upstream.apply_pin_updates(
            text,
            {
                "awx": {
                    "ref": "devel",
                    "commit": new_commit,
                    "public_image_digest": digest,
                }
            },
            updated="2026-09-29T00:00:00Z",
        )
        self.assertTrue(changed)
        self.assertIn("# Controller API image", new)
        self.assertIn("# Prefer setting commit for reproducible releases:", new)
        self.assertIn(f"commit: {new_commit}", new)
        self.assertNotIn(f"commit: {old_awx}", new)
        self.assertIn(f'public_image_digest: "{digest}"', new)
        self.assertIn("public_image: ghcr.io/ansible/jewel:latest", new)
        self.assertIn(f"commit: {old_jewel}", new)
        loaded = yaml.safe_load(new)
        self.assertEqual(loaded["components"]["awx"]["ref"], "devel")
        self.assertEqual(loaded["components"]["awx"]["commit"], new_commit)
        self.assertEqual(loaded["components"]["awx"]["public_image_digest"], digest)
        self.assertEqual(loaded["components"]["jewel"]["ref"], "devel")
        self.assertEqual(loaded["updated"], "2026-09-29T00:00:00Z")
        # Digest sits with the awx image, not after the component block.
        awx = new.split("  jewel:", 1)[0]
        self.assertIn("public_image_digest:", awx)
        again, changed_again = upstream.apply_pin_updates(
            new,
            {
                "awx": {
                    "ref": "devel",
                    "commit": new_commit,
                    "public_image_digest": digest,
                }
            },
            updated="2026-09-29T00:00:00Z",
        )
        self.assertFalse(changed_again)
        self.assertEqual(again, new)

    def test_stable_ref_is_rewritten_to_devel(self):
        text = (
            "components:\n"
            "  awx:\n"
            '    ref: "24.6.1"\n'
            "    commit: abcdefabcdefabcdefabcdefabcdefabcdefabcd\n"
            "    public_image: ghcr.io/ansible/awx:24.6.1\n"
        )
        digest = "sha256:" + "cd" * 32
        new, changed = upstream.apply_pin_updates(
            text,
            {
                "awx": {
                    "ref": "devel",
                    "commit": "e995e5fc5f92aaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "public_image": "ghcr.io/ansible/awx:devel",
                    "public_image_digest": digest,
                }
            },
            updated=None,
        )
        self.assertTrue(changed)
        loaded = yaml.safe_load(new)
        self.assertEqual(loaded["components"]["awx"]["ref"], "devel")
        self.assertEqual(
            loaded["components"]["awx"]["public_image"], "ghcr.io/ansible/awx:devel"
        )
        self.assertNotIn("24.6.1", new)
        self.assertEqual(loaded["components"]["awx"]["public_image_digest"], digest)

    def test_unchanged_pins_are_not_rewritten(self):
        text = (ROOT / "pins.yaml").read_text(encoding="utf-8")
        current = yaml.safe_load(text)["components"]["awx"]["commit"]
        new, changed = upstream.apply_pin_updates(
            text,
            {
                "awx": {
                    "ref": "devel",
                    "commit": current,
                }
            },
            updated="2099-01-01T00:00:00Z",
        )
        self.assertFalse(changed)
        self.assertEqual(new, text)


class CommitLogTest(unittest.TestCase):
    def test_subjects_are_the_changelog(self):
        info = {
            "commits": [
                {"sha": "a" * 40, "date": "2026-09-01", "subject": "Fix the gateway"},
                {"sha": "b" * 40, "date": "2026-09-02", "subject": "Add reports"},
            ],
            "truncated": False,
            "reached_base": True,
            "error": None,
        }
        text = "\n".join(
            upstream.format_commit_log(
                "ansible-ui",
                "devel",
                "c" * 40,
                "b" * 40,
                info,
                "ansible/ansible-ui",
            )
        )
        self.assertIn("Fix the gateway", text)
        self.assertIn("Add reports", text)
        self.assertIn("ansible/ansible-ui/commit/" + "a" * 40, text)
        self.assertIn("`devel`", text)


class ProposalNotesTest(unittest.TestCase):
    def test_proposal_rejects_stable_and_lists_commits(self):
        old_sha = "c" * 40
        new_sha = "b" * 40
        prev = {
            "published": {"platform-ui": {"version": "0.1.1"}},
            "components": {
                "ansible-ui": {
                    "repository": "https://github.com/ansible/ansible-ui.git",
                    "ref": "v2.4.313",
                    "commit": old_sha,
                }
            },
            "derived": {"platform-ui": {"release_triggers": ["ansible-ui"]}},
        }
        curr = {
            "published": {"platform-ui": {"version": "0.1.1"}},
            "components": {
                "ansible-ui": {
                    "repository": "https://github.com/ansible/ansible-ui.git",
                    "ref": "devel",
                    "commit": new_sha,
                },
                "awx": {
                    "repository": "https://github.com/ansible/awx.git",
                    "ref": "devel",
                    "commit": "d" * 40,
                    "build": False,
                    "public_image": "ghcr.io/ansible/awx:devel",
                    "public_image_digest": "sha256:" + "ab" * 32,
                },
            },
            "derived": {
                "platform-ui": {"release_triggers": ["ansible-ui"]},
                "awx": {"release_triggers": ["awx"]},
            },
        }
        # Previous awx pin absent, so the image table still renders from curr.
        logs = {
            "ansible-ui": {
                "commits": [
                    {
                        "sha": new_sha,
                        "date": "2026-09-28",
                        "subject": "fix(data-editor): stop the growth loop",
                    }
                ],
                "truncated": False,
                "reached_base": True,
                "error": None,
            }
        }
        lines, changes = render_notes.render_proposal(
            prev=prev,
            curr=curr,
            prev_name="pins.prev.yaml",
            curr_name="pins.proposed.yaml",
            commit_logs=logs,
        )
        text = "\n".join(lines)
        self.assertGreaterEqual(changes, 1)
        self.assertIn("stable and semver", text)
        self.assertIn("not candidates", text)
        self.assertIn("fix(data-editor): stop the growth loop", text)
        self.assertIn("Ignored previous ref `v2.4.313`", text)
        self.assertIn("`platform-ui-v0.1.2`", text)
        self.assertIn("sha256:" + "ab" * 32, text)
        self.assertIn("do not cut an awx image", text)
        self.assertNotIn("prefer semver", text.lower())
        self.assertNotIn("newest matching semver", text.lower())

    def test_next_patch(self):
        self.assertEqual(render_notes.next_patch("0.1.1"), "0.1.2")
        self.assertEqual(render_notes.next_patch(""), "X.Y.Z")

    def test_release_notes_include_upstream_commits_and_base_digest(self):
        old = "c" * 40
        new = "b" * 40
        digest = "sha256:" + "ab" * 32
        prev = {
            "components": {
                "ansible-ui": {
                    "repository": "https://github.com/ansible/ansible-ui.git",
                    "ref": "devel",
                    "commit": old,
                },
                "jewel": {
                    "repository": "https://github.com/ansible/jewel.git",
                    "ref": "devel",
                    "commit": old,
                    "public_image": "ghcr.io/ansible/jewel:latest",
                },
            }
        }
        curr = {
            "registry": {"prefix": "ghcr.io/flippyboy/awx"},
            "published": {
                "platform-ui": {"version": "0.1.1"},
                "jewel-with-ui": {"platform_ui_version": "0.1.1"},
            },
            "components": {
                "ansible-ui": {
                    "repository": "https://github.com/ansible/ansible-ui.git",
                    "ref": "devel",
                    "commit": new,
                },
                "jewel": {
                    "repository": "https://github.com/ansible/jewel.git",
                    "ref": "devel",
                    "commit": new,
                    "public_image": "ghcr.io/ansible/jewel:latest",
                    "public_image_digest": digest,
                },
            },
            "derived": {
                "platform-ui": {"release_triggers": ["ansible-ui"]},
                "jewel-with-ui": {"release_triggers": ["jewel"]},
            },
        }
        logs = {
            "ansible-ui": {
                "commits": [
                    {
                        "sha": new,
                        "date": "2026-09-28",
                        "subject": "feat: landing on devel",
                    }
                ],
                "truncated": False,
                "reached_base": True,
                "error": None,
            },
            "jewel": {
                "commits": [
                    {
                        "sha": new,
                        "date": "2026-09-28",
                        "subject": "feat: gateway username policy",
                    }
                ],
                "truncated": False,
                "reached_base": True,
                "error": None,
            },
        }
        ui_lines, ui_changes = render_notes.render_release(
            prev=prev,
            curr=curr,
            component="platform-ui",
            version="0.1.2",
            platform_ui_version="",
            registry_prefix="ghcr.io/flippyboy/awx",
            prev_name="pins.prev.yaml",
            curr_name="pins.yaml",
            commit_logs=logs,
        )
        ui = "\n".join(ui_lines)
        self.assertEqual(ui_changes, 1)
        self.assertIn("feat: landing on devel", ui)
        self.assertIn("## Upstream commits", ui)
        self.assertNotIn("24.6.1", ui)

        jewel_lines, _ = render_notes.render_release(
            prev=prev,
            curr=curr,
            component="jewel-with-ui",
            version="0.1.2",
            platform_ui_version="0.1.1",
            registry_prefix="ghcr.io/flippyboy/awx",
            prev_name="pins.prev.yaml",
            curr_name="pins.yaml",
            commit_logs=logs,
        )
        jewel = "\n".join(jewel_lines)
        self.assertIn("feat: gateway username policy", jewel)
        self.assertIn(f"ghcr.io/ansible/jewel:latest@{digest}", jewel)
        self.assertIn("Stable upstream version tags are not used.", jewel)


if __name__ == "__main__":
    unittest.main()
