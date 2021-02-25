import unittest
from fizzbuzz_checker import fizzbuzzchecker

class numTest(unittest.TestCase):

    def test_should_be_zero(self):
        actual = fizzbuzzchecker.is_bob(0)
        self.assertFalse(actual, None)