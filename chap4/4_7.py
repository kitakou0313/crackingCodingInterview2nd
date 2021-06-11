from typing import List, Dict, Set, Tuple
from libs.queue import StrQueue
import unittest

# 依存先->依存元のグラフを作り、幅探索して全ノード到達できたか探索
def calExecutionOrder(projects:List[str], dependencies:List[Tuple[str]]) -> List[str]:
    notDependingPros:Set[str] = set()
    graph:Dict[str, List[str]] = {}

    for pro in projects:
        graph[pro] = []
    
    for depending, depended in dependencies:
        if not(depended in graph):
            graph[depended] = []
        graph[depended].append(depending)

    for pro in projects:
        if len(graph[pro]) == 0:
            notDependingPros.add(pro)

    projectOrder:List[str] = []
    isDone:Set[str] = set()

    for startPro in notDependingPros:
        projectOrder.append(startPro)
        isDone.add(startPro)

        q = StrQueue()
        q.push(startPro)

        while not(q.isEmpty()):
            nowPro = q.pop()
            for nxtWork in graph[nowPro]:
                if nxtWork in isDone:
                    continue
                
                q.push(nxtWork)
                projectOrder.append(nxtWork)

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

        for project, depended in dependencies:
            assert actual.index(depended) < actual.index(project)

if __name__ == "__main__":
    unittest.main()