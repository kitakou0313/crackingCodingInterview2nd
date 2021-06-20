from typing import Set
import unittest
import itertools
from unittest.case import TestCase

def generateAllPermutationOfString(string:str) -> Set[str]:
    pass

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            "abc",
            "abcde"
        ]

        for testInput in testCases:
            expected = set(["".join(v) for v in itertools.permutations(testInput)])
            self.assertEqual(generateAllPermutationOfString(testInput), expected)

if __name__ == "__main__":
    unittest.main()