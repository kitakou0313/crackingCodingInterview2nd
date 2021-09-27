from typing import List
import unittest
from unittest.case import TestCase

# 含まれる文字と数字の数が等しくなるような最長部分配列の探索
# 文字は2種類だけでよい

def findLongestMatchSubarray(array:List[str]) -> int:
    """
    ブルートフォース O(n^3)
    """
    maxLen = 0
    for subArrayLength in range(1,len(array)):
        for startInd in range(0, len(array) - (subArrayLength - 1)):
            Anum = 0
            Bnum = 0
            for indInSubArray in range(startInd, startInd + subArrayLength):
                if array[indInSubArray] == "A":
                    Anum += 1
                else:
                    Bnum += 1
            if Anum == Bnum:
                maxLen = max(maxLen, subArrayLength)
    return maxLen


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