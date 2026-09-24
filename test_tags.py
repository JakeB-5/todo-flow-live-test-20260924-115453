import unittest

from tags import normalize_tags


class NormalizeTagsTest(unittest.TestCase):
    def test_strips_and_lowercases(self):
        self.assertEqual(normalize_tags([" Foo ", "BAR"]), ["foo", "bar"])

    def test_drops_empty_and_whitespace_only(self):
        self.assertEqual(normalize_tags(["", "  ", "a", "\t\n"]), ["a"])

    def test_removes_mixed_case_duplicates_preserving_first_order(self):
        self.assertEqual(
            normalize_tags(["B", "a", " b ", "A", "c", "a"]),
            ["b", "a", "c"],
        )

    def test_removes_exact_repeats(self):
        self.assertEqual(normalize_tags(["x", "x", "y", "x"]), ["x", "y"])

    def test_empty_input(self):
        self.assertEqual(normalize_tags([]), [])

    def test_accepts_any_iterable(self):
        self.assertEqual(normalize_tags((" Q ", "q")), ["q"])


if __name__ == "__main__":
    unittest.main()
