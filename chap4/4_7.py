from typing import List, Dict, Set, Tuple
import unittest
import heapq

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

class PriQueueEntry(object):
    """
    優先度付キュー用のエントリクラス
    """
    def __init__(self, data:str, inNum:int) -> None:
        super().__init__()
        self.data = data
        self.inNum = inNum

    def __lt__(self, other:'PriQueueEntry') -> bool:
        return self.inNum < other.inNum


# 依存先->依存元のグラフを作り、トポロジカルソートして返す
def calExecutionOrder(projects:List[str], dependencies:List[Tuple[str]]) -> List[str]:
    graph = constructGraph(projects, dependencies)
    inNumDict = countInMum(projects, dependencies)

    priQ:List[]

    projectOrder:List[str] = []
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