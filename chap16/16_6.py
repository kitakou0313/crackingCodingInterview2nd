from typing import List
import unittest

#O(n*log(n))
def searchMinDiff(listA:List[int], listB:List[int]) -> int:
    sortedA = sorted(listA)
    sortedB = sorted(listB)

    indInA = 0
    indInB = 0
    res = abs(sortedA[indInA] - sortedB[indInB])

    while indInA < len(sortedA) and indInB < len(sortedB):
        res = min(res, abs(sortedA[indInA] - sortedB[indInB]))
        if sortedA[indInA] < sortedB[indInB]:
            indInA+=1
        else:
            indInB+=1

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