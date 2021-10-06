from typing import List
import unittest

def findMajorityInArray(array:List[int]) -> int:
    """
    O(n)の実行時間, O(1)の空間計算量
    """
    maxNum = 0
    majority = -1

    for preMajorityInd in range(len(array)):
        count = 0
        for elementInd in range(len(array)):
            if array[preMajorityInd] == array[elementInd]:
                count += 1
        
        if count > majority:
            maxNum = count
            majority = array[preMajorityInd]

    if maxNum > int(len(array) / 2):
        return majority
    
    return -1

class Test(unittest.TestCase):
    """
    docstring
    """
    def test(self):
        """
        docstring
        """
        testCases = [
            ([1,2,5,9,5,9,5,5,5], 5)
        ]

        for input, expected in testCases:
            self.assertEqual(findMajorityInArray(input), expected)

if __name__ == "__main__":
    unittest.main()