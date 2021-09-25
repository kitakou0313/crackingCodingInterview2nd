import unittest
from unittest.case import TestCase

# 含まれる文字と数字の数が等しくなるような最長部分配列の探索
# 文字は2種類だけでよい

class Test(unittest.TestCase):
    """
    docstring
    """
    def test_1(self):
        testCase = [
            (["A", "B", "A", "A", "B", "B"],6),
            (["A", "B", "A", "B", "B", "B"], 4),
            (["B", "B", "B", "A", "B", "A"], 4)
        ]
        

if __name__ == "__main__":
    unittest.main()