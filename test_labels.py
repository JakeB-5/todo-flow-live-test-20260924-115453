import unittest

from labels import join_labels


class JoinLabelsFilteringTest(unittest.TestCase):
    def test_empty_input_returns_empty_string(self):
        self.assertEqual(join_labels([]), "")

    def test_drops_empty_and_whitespace_only_labels(self):
        self.assertEqual(join_labels(["", "  ", "a", "\t\n", "b"]), "a, b")

    def test_all_whitespace_returns_empty_string(self):
        self.assertEqual(join_labels([" ", "\t", ""]), "")

    def test_strips_surrounding_whitespace(self):
        self.assertEqual(join_labels(["  foo ", "\tbar\n"]), "foo, bar")

    def test_preserves_duplicates(self):
        self.assertEqual(join_labels(["x", "x", " x ", "y"]), "x, x, x, y")

    def test_preserves_mixed_case(self):
        self.assertEqual(
            join_labels(["Foo", "foo", " FOO ", "bAr"]),
            "Foo, foo, FOO, bAr",
        )

    def test_preserves_inner_whitespace(self):
        self.assertEqual(join_labels([" a  b ", "c"]), "a  b, c")

    def test_accepts_any_iterable(self):
        self.assertEqual(join_labels((" A ", "b")), "A, b")
        self.assertEqual(join_labels(s for s in ["p", " ", "q"]), "p, q")


class JoinLabelsSeparatorTest(unittest.TestCase):
    def test_default_separator_is_comma_space(self):
        self.assertEqual(join_labels(["a", "b", "c"]), "a, b, c")

    def test_single_label_has_no_separator(self):
        self.assertEqual(join_labels([" solo "]), "solo")

    def test_explicit_pipe_separator(self):
        self.assertEqual(join_labels(["a", " ", "B"], "|"), "a|B")

    def test_explicit_separator_keyword(self):
        self.assertEqual(join_labels(["a", "b"], separator=" / "), "a / b")

    def test_empty_separator(self):
        self.assertEqual(join_labels(["a", "b", "a"], separator=""), "aba")

    def test_newline_separator(self):
        self.assertEqual(join_labels(["a", "b"], separator="\n"), "a\nb")

    def test_label_containing_separator_text_is_kept(self):
        self.assertEqual(join_labels(["a, b", "c"]), "a, b, c")


if __name__ == "__main__":
    unittest.main()
