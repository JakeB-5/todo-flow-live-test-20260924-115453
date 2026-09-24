import unittest
from titles import normalize_title
from tags import normalize_tags

class Baseline(unittest.TestCase):
    def test_title(self):
        self.assertEqual(normalize_title(" hi "), "hi")
    def test_tags(self):
        self.assertEqual(normalize_tags(["a"]), ["a"])
