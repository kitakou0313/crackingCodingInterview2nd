from typing import Set
import unittest

def generateAllParensPattern(parensNum:int) -> Set[str]:
    if parensNum == 1:
        return set(["()"])

    #括弧の中、外でそれぞれ再帰的に追加していく
    parenPatterns = generateAllParensPattern(parensNum - 1)

    res:Set[str] = set()

    for paren in parenPatterns:
        res.add("()" + paren)
        res.add(paren + "()")
        res.add("(" + paren +")")

    return res


class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            (2, set(["()()", "(())"])),
            (3, set(["((()))", "(()())", "(())()", "()(())", "()()()"])),
        ]

        for testInput, expected in testCases:
            self.assertEqual(generateAllParensPattern(testInput), expected)

if __name__ == "__main__":
    unittest.main()