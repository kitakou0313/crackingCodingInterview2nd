from typing import List, Dict, Set, Tuple
import unittest
from libs.queue import StrQueue

def constructGraph(projects:List[str],dependencies:List[Tuple[str]]) -> Dict[str, List[str]]:
    graph:Dict[str, List[str]] = {}

    for From, to in dependencies:
        if From not in graph:
            graph[From] = []
        graph[From].append(to)

    for pro in projects:
        if not(pro in graph):
            graph[pro] = []

    return graph

def countInMum(projects:List[str], dependencies:List[Tuple[str]]) -> Dict[str, int]:
    inNumDict:Dict[str, int] = {}
    for pro in projects:
        inNumDict[pro] = 0

    for From, to in dependencies:
        inNumDict[to] += 1

    return inNumDict

def findProsToDo(q:StrQueue, inNumDict:Dict[str, int], didPros:Set[str]) -> None:
    for pro, inNum in inNumDict.items():
        if pro in didPros:
            continue
        if inNum == 0:
            q.push(pro)
            didPros.add(pro)

# 依存先->依存元のグラフを作り、トポロジカルソートして返す
def calExecutionOrder(projects:List[str], dependencies:List[Tuple[str]]) -> List[str]:
    graph = constructGraph(projects, dependencies)
    inNumDict = countInMum(projects, dependencies)

    proToDo = StrQueue()

    didPros:Set[str] = set()
    findProsToDo(proToDo, inNumDict, didPros)

    projectOrder:List[str] = []

    while not(proToDo.isEmpty()):
        proToDoNow = proToDo.pop()
        projectOrder.append(proToDoNow)

        for nxtPro in graph[proToDoNow]:
            inNumDict[nxtPro] -= 1

        findProsToDo(proToDo, inNumDict, didPros)

    return projectOrder

class Test(unittest.TestCase):
    def test1(self):
        projects:List[str] = ["a", "b", "c", "d", "e", "f", "g"]
        dependencies:List[Tuple[str]] = [
            ("d", "g"),
            ("a", "e"),
            ("b", "e"),
            ("c", "a"),
            ("f", "a"),
            ("b", "a"),
            ("f", "c"),
            ("f", "b"),
        ]

        actual = calExecutionOrder(projects, dependencies)

        for depended, project in dependencies:
            assert actual.index(depended) < actual.index(project)

if __name__ == "__main__":
    unittest.main()