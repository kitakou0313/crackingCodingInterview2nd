from typing import List, Dict, Tuple
import unittest

def calExecutionOrder(projects:List[str], graph:Dict[str, List[str]]) -> List[str]:
    return 

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