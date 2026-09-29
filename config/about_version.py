"""Named versions for the Platform UI About dialog.

The dialog title is "Ansible Automation Platform <gateway ping version>".
The Automation Controller row is the controller ping version.

Gateway `get_aap_version()` keeps only major.minor, so "0.1.1" would show
as "0.1". Replace `get_aap_version` itself.

Controller `get_awx_version()` prefers the installed `awx` package metadata
over `awx.__version__`. Replace `get_awx_version` on the utils modules the
ping view imports.
"""

import importlib.abc
import importlib.machinery
import os
import sys

PINS_PATH = "/etc/awx-platform/pins.yaml"

# Gateway image we ship. Its published version is the platform line.
PLATFORM_COMPONENT = "jewel-with-ui"
# Set only when an awx image is actually published. Otherwise the controller
# row uses the platform version (components.awx.build stays false).
CONTROLLER_COMPONENT = "awx"

_CONTROLLER_ATTR = "get_awx_version"
_PLATFORM_ATTR = "get_aap_version"

_CONTROLLER_MODULES = (
    "awx.main.utils.common",
    "awx.main.utils",
    "awx.api.views.root",
    "awx.api.generics",
    "awx.api.views.analytics",
)
_PLATFORM_MODULES = (
    "aap_gateway_api.version",
    "aap_gateway_api.views.api.v1.ping",
)

# module name -> {attribute: zero-arg function}
_PATCHES = {}
_FINDERS = set()


def pins_path(environ=None):
    env = os.environ if environ is None else environ
    return env.get("AWX_PLATFORM_PINS") or PINS_PATH


def published_value(text, component, key):
    """Value of `key` under `published.<component>`, ignoring comments."""
    in_published = False
    current = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            in_published = stripped == "published:"
            current = None
            continue
        if not in_published:
            continue
        name, sep, rest = stripped.partition(":")
        if not sep:
            continue
        if indent == 2 and not rest.strip():
            current = name
            continue
        if current == component and name == key:
            return _yaml_scalar(rest.strip())
    return ""


def resolve_platform_version(pins_text=None, environ=None):
    env = os.environ if environ is None else environ
    override = (env.get("PLATFORM_VERSION") or "").strip()
    if override:
        return override
    text = _pins_text(pins_text, env)
    return published_value(text, PLATFORM_COMPONENT, "version")


def resolve_controller_version(pins_text=None, environ=None):
    env = os.environ if environ is None else environ
    override = (env.get("CONTROLLER_VERSION") or "").strip()
    if override:
        return override
    text = _pins_text(pins_text, env)
    named = published_value(text, CONTROLLER_COMPONENT, "version")
    if named:
        return named
    return published_value(text, PLATFORM_COMPONENT, "version")


def install_platform_version(version=None, environ=None):
    resolved = resolve_platform_version(environ=environ) if version is None else version
    if not resolved:
        return ""
    _install(list(_PLATFORM_MODULES), _PLATFORM_ATTR, resolved)
    return resolved


def install_controller_version(version=None, environ=None):
    resolved = resolve_controller_version(environ=environ) if version is None else version
    if not resolved:
        return ""
    _install(list(_CONTROLLER_MODULES), _CONTROLLER_ATTR, resolved)
    return resolved


def _pins_text(pins_text, env):
    if pins_text is not None:
        return pins_text
    path = pins_path(env)
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError as exc:
        print(f"awx-platform: cannot read pins ({path}): {exc}", file=sys.stderr)
        return ""


def _yaml_scalar(raw):
    if raw[:1] in ("'", '"'):
        quote = raw[0]
        end = raw.find(quote, 1)
        if end != -1:
            return raw[1:end]
    if " #" in raw:
        raw = raw.split(" #", 1)[0]
    return raw.strip().strip("'\"")


def _constant(value):
    def _return_version():
        return value

    return _return_version


def _install(modules, attr, value):
    fn = _constant(value)
    for module_name in modules:
        bucket = _PATCHES.setdefault(module_name, {})
        bucket[attr] = fn
        loaded = sys.modules.get(module_name)
        if loaded is not None and hasattr(loaded, attr):
            setattr(loaded, attr, fn)
        if module_name not in _FINDERS:
            sys.meta_path.insert(0, _PatchFinder(module_name))
            _FINDERS.add(module_name)


class _PatchFinder(importlib.abc.MetaPathFinder):
    def __init__(self, module_name):
        self.module_name = module_name

    def find_spec(self, fullname, path, target=None):
        if fullname != self.module_name:
            return None
        spec = importlib.machinery.PathFinder.find_spec(fullname, path)
        if spec is None or spec.loader is None:
            return spec
        spec.loader = _PatchLoader(spec.loader, fullname)
        return spec


class _PatchLoader(importlib.abc.Loader):
    def __init__(self, inner, module_name):
        self._inner = inner
        self._module_name = module_name

    def create_module(self, spec):
        create = getattr(self._inner, "create_module", None)
        if create is None:
            return None
        return create(spec)

    def exec_module(self, module):
        self._inner.exec_module(module)
        for attr, fn in _PATCHES.get(self._module_name, {}).items():
            setattr(module, attr, fn)
