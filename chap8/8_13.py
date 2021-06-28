from typing import List
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

# ある箱を底とした時の最大の高さをメモ化して使う
def calHighestBoxStack(boxes:List[Box]) -> int:
    pass

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