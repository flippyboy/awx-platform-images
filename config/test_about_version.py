"""Version strings shown in the Platform UI About dialog."""

import importlib
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import about_version  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


class PublishedValueTest(unittest.TestCase):
    def test_real_pins_use_named_releases(self):
        text = (ROOT / "pins.yaml").read_text(encoding="utf-8")
        self.assertEqual(
            about_version.resolve_platform_version(text, environ={}),
            "0.1.2",
        )
        # published.awx.version is commented out; controller shares the platform name.
        self.assertEqual(
            about_version.resolve_controller_version(text, environ={}),
            "0.1.2",
        )
        self.assertEqual(about_version.published_value(text, "awx", "version"), "")

    def test_ignores_comments_and_sibling_keys(self):
        text = textwrap.dedent(
            """
            published:
              jewel-with-ui:
                version: "1.2.3"
                platform_ui_version: "9.9.9"
              # awx:
              #   version: "0.1.0"
            components:
              awx:
                version: "8.8.8"
            """
        )
        self.assertEqual(about_version.resolve_platform_version(text, environ={}), "1.2.3")
        self.assertEqual(about_version.resolve_controller_version(text, environ={}), "1.2.3")

    def test_published_awx_version_is_the_controller_line(self):
        text = textwrap.dedent(
            """
            published:
              jewel-with-ui:
                version: "1.2.3"
              awx:
                version: "4.5.6"
            """
        )
        self.assertEqual(about_version.resolve_controller_version(text, environ={}), "4.5.6")

    def test_env_overrides_pins(self):
        text = "published:\n  jewel-with-ui:\n    version: \"1.2.3\"\n"
        env = {"PLATFORM_VERSION": "2.5", "CONTROLLER_VERSION": "9.0.0"}
        self.assertEqual(about_version.resolve_platform_version(text, environ=env), "2.5")
        self.assertEqual(about_version.resolve_controller_version(text, environ=env), "9.0.0")

    def test_blank_env_falls_through(self):
        text = "published:\n  jewel-with-ui:\n    version: \"1.2.3\"\n"
        env = {"PLATFORM_VERSION": "  ", "CONTROLLER_VERSION": ""}
        self.assertEqual(about_version.resolve_platform_version(text, environ=env), "1.2.3")
        self.assertEqual(about_version.resolve_controller_version(text, environ=env), "1.2.3")


class InstallTest(unittest.TestCase):
    def test_platform_patch_keeps_patch_version(self):
        name = "aap_gateway_api.version"
        previous = sys.modules.get(name)
        module = type(sys)("aap_gateway_api.version")
        module.get_aap_version = lambda: ".".join("0.1.1".split(".")[:2])
        sys.modules[name] = module
        try:
            self.assertEqual(about_version.install_platform_version("0.1.1"), "0.1.1")
            self.assertEqual(module.get_aap_version(), "0.1.1")
        finally:
            if previous is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = previous

    def test_from_import_binds_the_named_version(self):
        module_name = "awx_platform_about_sample"
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, module_name + ".py").write_text(
                "def get_awx_version():\n    return '0.1.dev1+gdeadbeef'\n",
                encoding="utf-8",
            )
            sys.path.insert(0, tmp)
            try:
                about_version._install([module_name], "get_awx_version", "0.1.1")
                imported = importlib.import_module(module_name)
                self.assertEqual(imported.get_awx_version(), "0.1.1")
                # `from module import get_awx_version` copies the patched function.
                fresh = importlib.reload(imported)
                self.assertEqual(fresh.get_awx_version(), "0.1.1")
            finally:
                sys.path.remove(tmp)
                sys.modules.pop(module_name, None)

    def test_empty_version_does_not_patch(self):
        self.assertEqual(about_version.install_controller_version(""), "")


if __name__ == "__main__":
    unittest.main()
