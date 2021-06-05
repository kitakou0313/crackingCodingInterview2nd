from typing import Dict, List, Tuple
import unittest

def isHavingPathAtoB(graph:Dict[str, List[str]], A:str, B:str) -> bool:
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