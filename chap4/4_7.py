from typing import List, Dict, Set, Tuple
import unittest
import heapq

class nodeWithInNum(object):
    """
    入次数付有向グラフノード
    """
    def __init__(self) -> None:
        super().__init__()
        self.__inNum:int = 0
        self.__nextNodes:List[nodeWithInNum] = []

    def getInNum(self) -> int:
        return self.__inNum
    
    def getNextNodes(self) -> List['nodeWithInNum']:
        return self.__nextNodes

    def addNextNode(self, node:'nodeWithInNum'):
        """
        次ノード追加
        """
        self.__nextNodes.append(node)

def constructGrapth(dependencies:List[Tuple[str]]):
    return 

# 依存先->依存元のグラフを作り、トポロジカルソートして返す
def calExecutionOrder(projects:List[str], dependencies:List[Tuple[str]]) -> List[str]:
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