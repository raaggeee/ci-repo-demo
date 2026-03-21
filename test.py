import unittest
from app import add, sub, multi

class TestMathsFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)


    def test_sub(self):
        self.assertEqual(sub(3, 2), 1)


    def test_multi(self):
        self.assertEqual(multi(1, 2), 2)

if __name__ == "__main__":
    unittest.main()