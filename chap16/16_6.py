from typing import List
import unittest

#O(len(A)*len(B))
def searchMinDiff(listA:List[int], listB:List[int]) -> int:
    res = float("inf")

    for numA in listA:
        for numB in listB:
            res = min(res, abs(numA - numB))

    return res

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([1,3,15,11,2], [23,127,235,19,8], 3)
        ]

        for listA, listB, expected in testCases:
            self.assertEqual(searchMinDiff(listA, listB), expected)

        

if __name__ == "__main__":
    unittest.main()