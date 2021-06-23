from typing import Set, Tuple
import unittest
import copy
from libs.queue import TupleQueue

def fillMapWithColor(map, pos, color):
    res = copy.deepcopy(map)

    q = TupleQueue()
    isVisited:Set[Tuple[int]] = set()

    dyVec = [0,1,0,-1]
    dxVec = [1,0,-1,0]

    oriColor = map[pos[0]][pos[1]]

    q.push(pos)
    isVisited.add(pos)

    while not(q.isEmpty()):
        nowY, nowX = q.pop()
        res[nowY][nowX] = color

        for dVecInd in range(len(dxVec)):
            nxtY = nowY + dyVec[dVecInd]
            nxtX = nowX + dxVec[dVecInd]

            if 0 <= nxtY <= len(res)-1 and 0 <= nxtX <= len(res[0])-1:
                if res[nxtY][nxtX] == oriColor:
                    q.push((nxtY, nxtX)) 
                    isVisited.add((nxtY, nxtX))

    return res

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([
                [0,1,1,1,1,1,0],
                [0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0],
                [0,1,1,1,1,1,0],
            ], (2,3), 1, 
            [
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
            ]
            )
        ]

        for [oriMap, pos, color, expected] in testCases:
            self.assertEqual(fillMapWithColor(oriMap, pos, color), expected)


if __name__ == "__main__":
    unittest.main()