import unittest
from titles import normalize_title


class NormalizeTitleSpaces(unittest.TestCase):
    def test_repeated_spaces(self):
        self.assertEqual(normalize_title("a  b"), "a b")

    def test_tab(self):
        self.assertEqual(normalize_title("a\tb"), "a b")

    def test_newline(self):
        self.assertEqual(normalize_title("a\nb"), "a b")

    def test_mixed_runs_and_edges(self):
        self.assertEqual(normalize_title("  a \t\n b  c "), "a b c")

    def test_crlf_and_tab(self):
        self.assertEqual(normalize_title("a\r\n\tb"), "a b")

    def test_baseline_trim(self):
        self.assertEqual(normalize_title(" hi "), "hi")


class NormalizeTitleEmpty(unittest.TestCase):
    def test_whitespace_only(self):
        self.assertEqual(normalize_title("   \t\n "), "")

    def test_empty_string(self):
        self.assertEqual(normalize_title(""), "")


if __name__ == "__main__":
    unittest.main()
