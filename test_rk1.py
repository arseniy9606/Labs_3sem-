import unittest

from rk1_refactored import (
    get_test_data,
    build_relations,
    query_d1,
    query_d2,
    query_d3,
)


class TestRk1Queries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        langs, constructions, lang_syntax = get_test_data()
        one_to_many, many_to_many = build_relations(
            langs, constructions, lang_syntax
        )
        cls.langs = langs
        cls.one_to_many = one_to_many
        cls.many_to_many = many_to_many

    def test_query_d1(self):
        result = query_d1(self.one_to_many)

        expected = [
            ("condition", "Python"),
            ("iteration", "Python"),
            ("recursion", "Java"),
        ]

        self.assertEqual(result, expected)

    def test_query_d2(self):
        result = query_d2(self.langs, self.one_to_many)

        expected = [
            ("Ada", 2.0),
            ("Python", 3.0),
            ("Java", 4.0),
        ]

        self.assertEqual(result, expected)

    def test_query_d3(self):
        result = query_d3(self.langs, self.many_to_many)

        self.assertIn("Ada", result)
        self.assertIn("Assembly", result)

        self.assertEqual(
            result["Ada"],
            ["condition", "function definition"]
        )
        self.assertEqual(
            result["Assembly"],
            []
        )


if __name__ == "__main__":
    unittest.main()
