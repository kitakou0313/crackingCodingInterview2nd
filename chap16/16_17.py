from typing import List
import unittest

#合計が負の値or0になった区間を削除していく O(n)
def searchSumMaxInterval(array:List[int]) -> int:
    maxSum = - float("inf")

    internalStartInd = 0
    internalEndInd = 0
    sumInInternal = 0

    while (internalStartInd < len(array)) and (internalEndInd < len(array)):
        sumInInternal += array[internalEndInd]
        if sumInInternal <= 0:
            internalStartInd = internalEndInd + 1
            internalEndInd = internalStartInd
            sumInInternal = 0
        else:
            maxSum = max(maxSum, sumInInternal)
            internalEndInd += 1
            
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