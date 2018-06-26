from unittest import TestCase

from palindrome.palindrome import Palindrome


class PalindromeTest(TestCase):

    def setUp(self):
        self.check_palindrome = Palindrome()

    def test_should_be_ok_when_check_is_palindrome(self):
        self.assertTrue(self.check_palindrome.is_palindrome('reconocer'))

    def test_should_be_ok_when_check_is_palindrome(self):
        self.assertTrue(self.check_palindrome.is_palindrome('reconocer'))


    def tearDown(self):
        del self.check_palindrome
