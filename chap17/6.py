import unittest
from unittest.case import TestCase

def countNumberOf2(N:int) -> int:
    """
    Nまでの自然数で文字列表記したときの2の個数
    """
    return 2

class Test(TestCase):
    """
    docstring
    """
    def test(self):
        """
        docstring
        """
        testCases = [
            (25, 9)
        ]

        for input, expected in testCases:
            self.assertEqual(countNumberOf2(input), expected)

if __name__ == "__main__":
    unittest.main()