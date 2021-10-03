from typing import Dict, Tuple, List
from unittest import TestCase
import unittest

def calMaxHeightWithBottom(peopleList:List[Tuple[int]], bottom:Tuple[int] ,memo:Dict[Tuple[int], int]) -> int:
    """
    docstring
    """
    return 0

def calMaxTowerHeight(peopleList:List[Tuple[int]]) -> int:
    """
    全順序、全選び方について探索 O(2^n * nCn)
    memo化で高速化出来そう 各人が底の時の最大の高さをmemoにする
    """
    maxHeight = -float("inf")
    memo:Dict[Tuple[int], int] = {}

    for i in range(0, len(maxHeight)):
        lastPeoples = maxHeight[:i] + maxHeight[i+1:]
        maxHeight = max(maxHeight, calMaxHeightWithBottom(lastPeoples, peopleList[i], memo))

    return maxHeight

def isStandOnA(A:Tuple[int], B:Tuple[int]) -> bool:
    """
    AがBの上に立てるか判定
    """
    return A[0] < B[0] and A[1] < B[1]

class Test(TestCase):
    """
    docstring
    """
    def test(self):
        """
        docstring
        """
        testCases = [
            ([(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)],6)
        ]

        for inputtedCase, expected in testCases:
            self.assertEqual(calMaxTowerHeight(inputtedCase), expected)

if __name__ == "__main__":
    unittest.main()