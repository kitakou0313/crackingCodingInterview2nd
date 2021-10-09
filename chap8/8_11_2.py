from typing import Dict, List, Set
import unittest


def conuntNumberOfWayToPayN(payment: int, coins: List[int]) -> int:
    """
    paymentをコインで支払う場合の支払い方の数を計算
    """
    def helper(payment: int, coins: List[int], memo: Dict[int, Set[Set[int]]]) -> Set[Set[int]]:
        """
        hepler用関数、memoに追加済みならキャッシュを返す
        memoは金額に対する支払い方法の数を返す
        """
        res = 0
        for coin in coins:
            trgPayment = payment - coin

            if trgPayment < 0:
                continue

            if trgPayment in memo:
                res += memo[trgPayment]
            else:
                res += helper(trgPayment, coins, memo)

        memo[payment] = res
        return res

    memo = {}
    memo[0] = 1
    return len(helper(payment, coins, memo))


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
            self.assertEqual(conuntNumberOfWayToPayN(
                trgInput, coins), expected)


if __name__ == "__main__":
    unittest.main()
