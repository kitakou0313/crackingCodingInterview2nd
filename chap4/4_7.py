from typing import List, Dict, Set, Tuple
from libs.queue import StrQueue
import unittest

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