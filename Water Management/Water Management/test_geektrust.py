import unittest
from geektrust import main
import sys

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        expected_output = "2400 5215"
        self.assertEqual(main("instructions0.txt"), expected_output)

    def test_two(self):
        expected_output = "3000 5750"
        self.assertEqual(main("instructions1.txt"), expected_output)

    def test_three(self):
        expected_output = "900 1200"
        self.assertEqual(main("instructions2.txt"), expected_output)

    def test_four(self):
        expected_output = "5400 24475"
        self.assertEqual(main("instructions3.txt"), expected_output)

    def test_five(self):
        expected_output = "3900 10334"
        self.assertEqual(main("instructions4.txt"), expected_output)


if __name__ == '__main__':
    unittest.main()
