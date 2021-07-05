from typing import List, Set, Tuple
from libs.queue import TupleQueue
import unittest
from unittest.case import TestCase

# 
def calPondSize(map:List[List[int]], startInd:Tuple[int], visitedPondCoods:Set[Tuple[int]]) -> int:
    """
    池のサイズを返す
    """
    Y = len(map) - 1
    X = len(map[0]) -1
    dxVecs = [0,1,-1]
    dyVecs = [0,1,-1]

    pondCoodsSet:Set[Tuple[int]] = set()
    q = TupleQueue()

    q.push(startInd)
    pondCoodsSet.add(startInd)

    while not(q.isEmpty()):
        nowY, nowX = q.pop()

        for dx in dxVecs:
            for dy in dyVecs:
                if dx == 0 and dy == 0:
                    continue
                nxtY = nowY + dy
                nxtX = nowX + dx

                if 0 <= nxtY <= Y and 0 <= nxtX <= X:
                    if map[nxtY][nxtX] == 0 and not((nxtY, nowX) in pondCoodsSet) and not((nxtY, nxtX) in visitedPondCoods):
                        q.push((nxtY, nxtX))
                        pondCoodsSet.add((nxtY, nxtX))
                        visitedPondCoods.add((nxtY, nxtX))

    return len(pondCoodsSet)

#池毎に幅探索で探索する
def calAllPondSize(map:List[List[int]]) -> Set[int]:
    sizeSet:Set[int] = set()

    Y = len(map)
    X = len(map[0])

    visitedPondCoods = set()

    for y in range(Y):
        for x in range(X):
            if map[y][x] == 0:
                if (y, x) not in visitedPondCoods:
                    sizeSet.add(calPondSize(map, (y,x), visitedPondCoods))

    return sizeSet

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([
                [0,2,1,0],
                [0,1,0,1],
                [1,1,0,1],
                [0,1,0,1]
            ], set([2,4,1]))
        ]

        for inputtedMap, expected in testCases:
            self.assertEqual(calAllPondSize(inputtedMap), expected)

if __name__ == "__main__":
    unittest.main()