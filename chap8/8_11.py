from typing import Dict, List, Set, Tuple
import unittest

def calculateCoinsWithMemo(value:int, coins:List[int], memo:Dict[int, Set[Tuple[int]]]) -> Set[Tuple[int]]:
    """
    メモ化再帰
    """
    if value == 0:
        return set([(0 for _ in range(len(coins)))])

    res:Set[Tuple[int]] = set()
    for coinInd in range(len(coins)):
        restVal = value - coins[coinInd]

        if restVal < 0:
            continue
        
        restValResults = calculateCoinsWithMemo(restVal, coins, memo)    

        for restValRes in restValResults:
            tmp = list(restValRes)
            tmp[coinInd] += 1
            res.add(tuple(tmp))

    memo[value] = res
    return res

#メモ化再帰で頑張る
def calculateCoins(value:int, coins:List[int]) -> Set[Tuple[int]]:
    memo = {}
    return calculateCoinsWithMemo(value, coins, memo)

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            (1, 1),
            (4, 1),
            (5, 2),
            (15, 6),
            (20, 9)
        ]

        coins = [
            1,5,10,25
        ]

        for value, expected in testCases:
            res = calculateCoins(value, coins)
            print(res)
            self.assertEqual(len(res), expected)
            
if __name__ == "__main__":
    unittest.main()