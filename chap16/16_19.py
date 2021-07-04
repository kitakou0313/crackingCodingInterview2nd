from typing import List, Set
import unittest
from unittest.case import TestCase

#池毎に幅探索で探索する 池の座標をSetで返してそのサイズをカウントする
def calAllPondSize(map:List[List[int]]) -> Set[int]:
    pass

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([
                [0,2,1,0],
                [0,1,0,1],
                [1,1,0,1],
                [0,1,0,1]
            ], set([2,4,1]))
        ]

        for inputtedMap, expected in testCases:
            self.assertEqual(calAllPondSize(inputtedMap), expected)

if __name__ == "__main__":
    unittest.main()