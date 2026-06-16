import unittest

from hermes_workflow.primitives import filter_primitives, primitive_paths, slugify


class PrimitiveTests(unittest.TestCase):
    def test_starter_includes_johnny_decimal_para_and_gtd(self):
        systems = {primitive.system for primitive in filter_primitives("starter")}

        self.assertIn("johnny-decimal", systems)
        self.assertIn("para", systems)
        self.assertIn("gtd", systems)

    def test_primitive_paths_are_relative(self):
        paths = primitive_paths()

        self.assertIn("00-inbox", {str(path) for path in paths})
        self.assertTrue(all(not path.is_absolute() for path in paths))

    def test_slugify_is_filesystem_safe(self):
        self.assertEqual(slugify("My Local AI Inbox!"), "my-local-ai-inbox")

    def test_unknown_preset_is_rejected(self):
        with self.assertRaises(ValueError):
            filter_primitives("unknown")
