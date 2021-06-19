from typing import List, Set, Tuple
import unittest

def convertBitToIndex(bitInt:int) -> Set[int]:
    res = set()

    index = 0
    while bitInt != 0:
        if bitInt & 1 == 1:
            res.add(index)
        bitInt = bitInt >> 1
        index += 1

    return res

def generateAllSubset(universalSet:List[int]) -> Set[Tuple[int]]:
    numberElement = len(universalSet)

    resSet:Set[Tuple[int]] = set()

    for bitNum in range(0, 2 ** numberElement):
        indexes = convertBitToIndex(bitNum)

        subset = []
        for index in indexes:
            subset.append(universalSet[index])

        subset = tuple(subset)
        
        resSet.add(subset)

    return resSet

class Test(unittest.TestCase):
    def test1(self):

        testcases = [
            ([1,2,3],{(), (1,), (2,), (3,), (1,2), (2,3),(1,3), (1,2,3)}),
            ([1,2],{(), (1,), (2,), (1,2)})
        ]

        for testInput, expected in testcases:
            self.assertEqual(generateAllSubset(testInput), expected)


if __name__ == "__main__":
    unittest.main()