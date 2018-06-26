from unittest import TestCase

from palindrome.palindrome import Palindrome


class PalindromeTest(TestCase):

    def setUp(self):
        self.check_palindrome = Palindrome()

    def test_should_be_return_true_when_check_is_palindrome(self):
        self.assertTrue(self.check_palindrome.is_palindrome('reconocer'))

    def test_should_be_return_false_when_check_is_palindrome(self):
        self.assertFalse(self.check_palindrome.is_palindrome('persona'))

    def test_should_be_return_false_when_check_is_palindrome_with_upper_case_and_space(self):
        self.assertFalse(self.check_palindrome.is_palindrome('Se es o no se es'))

    def test_should_be_return_true_when_check_is_palindrome_space_and_upper_with_palindrome(self):
        self.assertTrue(self.check_palindrome.is_palindrome_space_and_upper('Se es o no se es'))

    def test_should_be_return_false_when_check_is_palindrome_space_and_upper_with_anything_word(self):
        self.assertFalse(self.check_palindrome.is_palindrome_space_and_upper('persona'))

    def test_should_be_return_true_when_check_simple_is_palindrome_(self):
        self.assertTrue(self.check_palindrome.simple_is_palindrome('reconocer'))

    def test_should_be_return_false_when_check_simple_is_palindrome(self):
        self.assertFalse(self.check_palindrome.simple_is_palindrome('persona'))

    def tearDown(self):
        del self.check_palindrome
