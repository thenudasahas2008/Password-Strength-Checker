"""Unit tests for the password strength checker."""

import unittest

from password_checker import assess_password


class PasswordCheckerTests(unittest.TestCase):
    def test_common_password_is_weak(self):
        result = assess_password("password")
        self.assertEqual(result["label"], "Weak")
        self.assertEqual(result["score"], 0)

    def test_short_password_is_not_strong(self):
        result = assess_password("Ab1!")
        self.assertNotEqual(result["label"], "Strong")

    def test_long_varied_password_can_be_strong(self):
        result = assess_password("R7!mQ2#vL9@pT4$xZ8")
        self.assertEqual(result["label"], "Strong")

    def test_returns_expected_keys(self):
        result = assess_password("example-password-2026")
        self.assertEqual(set(result.keys()), {"score", "label", "feedback"})
        self.assertIsInstance(result["feedback"], list)

    def test_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            assess_password(None)


if __name__ == "__main__":
    unittest.main()
