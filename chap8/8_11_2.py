from typing import List
import unittest


def conuntNumberOfWayToPayN(payment: int, coins: List[int]) -> int:
    """
    paymentをコインで支払う場合の支払い方の数を計算
    """
    pass


class Test(unittest.TestCase):
    """
    テストケース
    """

    def test(self):
        """
        テストケース
        """
        testCases = [
            (1, 1),
            (4, 1),
            (5, 2),
            (15, 6),
            (20, 9)
        ]

        coins = [
            1, 5, 10, 25
        ]

        for trgInput, expected in testCases:
            pass


if __name__ == "__main__":
    pass
