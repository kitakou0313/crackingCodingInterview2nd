from typing import Dict, List, Set, Tuple
import unittest


def conuntNumberOfWayToPayN(payment: int, coins: List[int]) -> int:
    """
    paymentをコインで支払う場合の支払い方の数を計算
    """
    def helper(payment: int, coins: List[int], memo: Dict[int, Set[Tuple[int]]]) -> Set[Tuple[int]]:
        """
        hepler用関数、memoに追加済みならキャッシュを返す
        memoは金額に対する支払い方法の数を返す
        """
        res: Set[Tuple[int]] = set()

        for coinInd in range(len(coins)):
            trgPayment = payment - coins[coinInd]

            if trgPayment < 0:
                continue

            trgAnsPaymentList = memo[trgPayment] if trgPayment in memo else helper(
                trgPayment, coins, memo)

            for paymentWay in trgAnsPaymentList:
                addedPayment = list(paymentWay)
                addedPayment[coinInd] += 1
                res.add(tuple(addedPayment))

        memo[payment] = res
        return res

    memo = {}
    fundList = tuple([0 for _ in range(len(coins))])
    memo[0] = set()
    memo[0].add(fundList)
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
