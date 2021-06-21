from typing import Dict, Set, List
import unittest
import itertools

def generatePermutationsWithoutDup(inputStr:str, memo:Dict[str, Set[str]]) -> Set[str]:
    if len(inputStr) == 1:
        memo[inputStr] = set([inputStr])
        return set([inputStr])

    res:Set[str] = set()
    chars:List[str] = list(inputStr)

    for charInd in range(0, len(chars)):
        restStr = "".join(chars[:charInd] + chars[charInd+1:])

        if restStr in memo:
            permsWithRestStr = memo[restStr]
        else:
            permsWithRestStr = generatePermutationsWithoutDup(restStr, memo)

        for perm in permsWithRestStr:
            res.add(chars[charInd] + perm)

        memo[inputStr] = res
    
    return res

#重複ありの場合に高速化させる
def generateAllPermutationOfString(inputStr:str) -> Set[str]:
    memo:Dict[str, Set[str]] = {}

    inputStr = "".join(sorted(inputStr))

    return generatePermutationsWithoutDup(inputStr, memo)

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            "abc",
            "abcde",
            "bab",
            "aaaaaa"
        ]

        for testInput in testCases:
            expected = set(["".join(v) for v in itertools.permutations(testInput)])
            self.assertEqual(generateAllPermutationOfString(testInput), expected)

if __name__ == "__main__":
    unittest.main()