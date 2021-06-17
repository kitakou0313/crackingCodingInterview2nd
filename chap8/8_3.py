from typing import List
import unittest
from unittest.case import TestCase

NOTFOUND = -1

#O(n)
def findMagicIndex(array:List[int]) -> int:
    for ind in range(len(array)):
        if ind == array[ind]:
            return ind

    return NOTFOUND


class Test(unittest.TestCase):
    def test1(self):
        testCase = [
            ([-11, 0, 2, 6,7,10], 2),
            ([-11, -10, -9, 10, 11], NOTFOUND)
        ]
        for inputCase, excepted in testCase:
            self.assertEqual(findMagicIndex(inputCase), excepted)

if __name__ == "__main__":
    unittest.main()