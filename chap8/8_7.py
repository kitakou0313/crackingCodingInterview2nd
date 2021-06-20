from typing import Set, List
import unittest
import itertools

def generateAllPermutationOfString(inputStr:str) -> Set[str]:
    if len(inputStr) == 1:
        return set([inputStr])

    res:Set[str] = set()

    chars:List[str] = list(inputStr)

    for charInd in range(0, len(chars)):
        permsOfRestString = generateAllPermutationOfString("".join(chars[:charInd] + chars[charInd+1:]))
        for perm in permsOfRestString:
            res.add(chars[charInd] + perm)

    return res

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