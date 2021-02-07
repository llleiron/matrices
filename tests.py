import unittest
from matrix import matrix

a = matrix([[5, 2],[7, 1]])
class TestMatrix(unittest.TestCase):
    def test_add(self):
        self.assertEqual(a.__add__([[5, 2],[7, 1]]), [[10, 4], [14, 2]])
