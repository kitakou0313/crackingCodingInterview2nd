from typing import List
import unittest

def calNumOfWaysToNstep(N:int) -> int:

    # dp[n]...nまでの行き方
    dp:List[int] = [0 for _ in range(N+1)]
    dp[0] = 1

    for n in range(0, N + 1):
        if n + 1 <= N:
            dp[n+1] += dp[n]
        if n + 2 <= N:
            dp[n+2] += dp[n]
        if n + 3 <= N:
            dp[n+3] += dp[n]        

    return dp[N]

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(calNumOfWaysToNstep(3), 4)
        self.assertEqual(calNumOfWaysToNstep(7), 44)

if __name__ == "__main__":
    unittest.main()