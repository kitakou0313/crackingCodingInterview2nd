from typing import Set
import unittest


def generateAllParensPatterns(n: int) -> Set[str]:
    """
    n組の括弧を使って生成できる括弧が成立した文字列の集合を求める関数
    """
    if n == 1:
        return set(["()"])

    n_1Reses = generateAllParensPatterns(n-1)

    res: Set[str] = set()

    for n_1Res in n_1Reses:
        res.add(n_1Res + "()")
        res.add("("+n_1Res+")")
        res.add("()" + n_1Res)

    return res


class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            (2, set(["()()", "(())"])),
            (3, set(["((()))", "(()())", "(())()", "()(())", "()()()"])),
        ]

        for testInput, expected in testCases:
            self.assertEqual(generateAllParensPatterns(testInput), expected)


if __name__ == "__main__":
    unittest.main()
