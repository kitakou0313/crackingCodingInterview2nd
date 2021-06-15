from typing import List, Set, Tuple
import unittest
from libs.queue import TupleQueue

def findPath(map:List[List[int]]) -> bool:
    """
    経路探索
    """
    R = len(map)
    C = len(map[0])

    dvecY:List[int] = [0, 1]
    dvecX:List[int] = [1, 0]

    isVisited:Set[Tuple[int]] = set()
    q = TupleQueue()

    isVisited.add((0, 0))
    q.push((0,0))

    while not(q.isEmpty()):
        now = q.pop()
        if now[0] == R-1 and now[1] == C-1:
            return True

        for dvecInd in range(len(dvecX)):
            nxtY = now[0] + dvecY[dvecInd]
            nxtX = now[1] + dvecX[dvecInd]

            if (0 <= nxtX and nxtX <= C - 1) and (0 <= nxtY and nxtY <= R-1) and map[nxtY][nxtX] == 0:
                if not((nxtY, nxtX) in isVisited):
                    isVisited.add((nxtY, nxtX))
                    q.push((nxtY, nxtX))

    return False

class Test(unittest.TestCase):
    def test1(self):
        map1 = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(findPath(map1), True)

        map2 = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [1,1,1,1,1],
            [0,0,0,0,0]
        ]
        self.assertEqual(findPath(map2), False)

if __name__ == "__main__":
    unittest.main()