from typing import List
import unittest

#2重ループで全区間探索O(n^2)
def searchSumMaxInterval(array:List[int]) -> int:
    maxSum = - float("inf")

    for intervalStartInd in range(0,len(array)):
        sumInInterval = 0
        for intervalEndInd in range(intervalStartInd, len(array)):
            sumInInterval += array[intervalEndInd]
            maxSum = max(maxSum, sumInInterval)

    return maxSum

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([2,-8,3,-2,4,-10], 5)
        ]

        for array, expected in testCases:
            self.assertEqual(searchSumMaxInterval(array), expected)

        

if __name__ == "__main__":
    unittest.main()