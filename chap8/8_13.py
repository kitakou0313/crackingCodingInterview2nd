from typing import Dict, List
import unittest

class Box(object):
    """
    箱クラス
    """
    def __init__(self, hi:int,wi:int, di:int) -> None:
        super().__init__()
        self.hi = hi
        self.wi = wi
        self.di = di

def calHighestBoxStackHelper(bottomBox:Box, boxes:List[Box], memo:Dict[Box, int]) -> int:
    """
    ヘルパー用関数
    """
    if bottomBox in memo:
        return memo[bottomBox]

    res = bottomBox.hi

    for nextBox in boxes:
        if nextBox.wi < bottomBox.wi and nextBox.hi < bottomBox.hi and nextBox.di < bottomBox.di:
            res = max(res, bottomBox.hi + calHighestBoxStackHelper(nextBox, boxes, memo))

    memo[bottomBox] = res
    return res


# ある箱を底とした時の最大の高さをメモ化して使う
def calHighestBoxStack(boxes:List[Box]) -> int:
    memo:Dict[Box, int] = {}

    maxHighest = -1
    for box in boxes:
        maxHighest = max(maxHighest, calHighestBoxStackHelper(box, boxes, memo))

    return maxHighest

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([Box(4,3,2),Box(5,4,1)], 5),
            ([Box(3,2,1), Box(6,5,4)],9),
            ([Box(100, 100, 100), Box(25, 25, 25), Box(20, 5, 30), Box(17, 4, 28)], 137)
        ]
        
        for boxes, expected in testCases:
            self.assertEqual(calHighestBoxStack(boxes), expected)
    
if __name__ == "__main__":
    unittest.main()