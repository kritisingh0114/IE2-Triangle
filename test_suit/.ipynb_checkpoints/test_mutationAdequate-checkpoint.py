import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class MutationCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(-1, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test2(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    def test3(self):
        actual = Triangle.classify(15, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def test4(self):
        actual = Triangle.classify(10, 15, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def test5(self):
        actual = Triangle.classify(10, 10, 15)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def test6(self):
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test7(self):
        actual = Triangle.classify(15, 20, 25)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    def test8(self):
        actual = Triangle.classify(5, 10, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test9(self):
        actual = Triangle.classify(10, 10, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test9(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test10(self):
        actual = Triangle.classify(10, 0, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test10(self):
        actual = Triangle.classify(10, 10, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test11(self):
        actual = Triangle.classify(3, 4, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test12(self):
        actual = Triangle.classify(3, 7, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test13(self):
        actual = Triangle.classify(7, 3, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test14(self):
        actual = Triangle.classify(20, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test15(self):
        actual = Triangle.classify(10, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test16(self):
        actual = Triangle.classify(7, -1, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
