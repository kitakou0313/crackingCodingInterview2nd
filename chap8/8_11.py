from typing import List
import unittest

def calculateCoins(value:int, coins:List[int]):
    pass

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            10, 20, 50
        ]

        coins = [
            1,5,10,25
        ]

        for n in testCases:
            print(calculateCoins(n, coins))

if __name__ == "__main__":
    unittest.main()