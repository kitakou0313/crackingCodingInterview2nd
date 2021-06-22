from typing import Set
import unittest

def generateAllParensPattern(parensNum:int) -> Set[str]:
    pass

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