import unittest
from geektrust import run
import sys

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        expected_output = 'C-Cave D-Tower G-Mansion\nC-Cave\nNO_VACANT_ROOM\nG-Mansion\nD-Tower\nC-Cave\nD-Tower\nINCORRECT_INPUT\nC-Cave G-Mansion\nC-Cave\nG-Mansion\nG-Mansion\nNO_VACANT_ROOM'
        self.assertEqual(run("input1.txt"), expected_output)

    def test_two(self):
        expected_output = 'C-Cave\nC-Cave\nINCORRECT_INPUT\nD-Tower\nG-Mansion\nG-Mansion\nG-Mansion\nNO_VACANT_ROOM\nD-Tower\nNO_VACANT_ROOM\nINCORRECT_INPUT'
        self.assertEqual(run("input2.txt"), expected_output)

    def test_three(self):
        expected_output = 'C-Cave D-Tower G-Mansion\nD-Tower\nG-Mansion\nD-Tower\nC-Cave\nINCORRECT_INPUT'
        self.assertEqual(run("input3.txt"), expected_output)

    def test_four(self):
        expected_output = 'C-Cave\nD-Tower\nG-Mansion\nC-Cave\nG-Mansion\nC-Cave D-Tower'
        self.assertEqual(run("input4.txt"), expected_output)


if __name__ == '__main__':
    unittest.main()
