from typing import Dict, List, Set, Tuple
import unittest
from libs.queue import StrQueue

#幅探でやる
def isHavingPathAtoB(graph:Dict[str, List[str]], A:str, B:str) -> bool:
    visitedNodes:Set[str] = set()
    q = StrQueue()

    visitedNodes.add(A)
    q.push(A)

    while not(q.isEmpty()):
        nowNode:str = q.pop()

        if nowNode == B:
            return True

        for nxtNode in graph[nowNode]:
            if not(nxtNode in visitedNodes):
                visitedNodes.add(nxtNode)
                q.push(nxtNode)

    return False

class Test(unittest.TestCase):
    def test1(self):
        graph:Dict[str, List[str]] = {
            "1":["2"],
            "2":["3", "4"],
            "3":[],
            "4":["5"],
            "5":["6"],
            "6":["4"]
        }

        testCases = [
            (("1", "2"), True),
            (("1", "3"), True),
            (("2", "5"), True),
            (("4", "6"), True),
            (("3", "4"), False),
            (("3", "6"), False)
        ]

        for testInput, expected in testCases:
            self.assertEqual(isHavingPathAtoB(graph, testInput[0], testInput[1]), expected)

if __name__ == "__main__":
    unittest.main()