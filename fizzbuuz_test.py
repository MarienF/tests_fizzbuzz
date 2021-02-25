import unittest
from fizzbuzz_checker import fizzbuzzchecker

class numTest(unittest.TestCase):

    def test_should_be_zero(self):
        with self.assertRaises(Exception):
            fizzbuzzchecker.is_bob(0)

    def test_should_be_negative(self):
        with self.assertRaises(Exception):
            fizzbuzzchecker.is_bob(-1)

    def test_shoud_be_multiple_of_3(self):
        actual = fizzbuzzchecker.is_bob(3)
        self.assertTrue(actual)

    def test_shoud_be_multiple_of_5(self):
        actual = fizzbuzzchecker.is_bob(5)
        self.assertTrue(actual)

    def test_should_be_multiple_of_3_and_5(self):
        actual = fizzbuzzchecker.is_bob(15)
        self.assertTrue(actual)

    def test_should_be_something_else(self):
        actual = fizzbuzzchecker.is_bob(14)
        self.assertFalse(actual)