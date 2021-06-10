from typing import List, Dict
import unittest

def calExecutionOrder(graph:Dict[str, List[str]]) -> List[str]:
    return 

class Test(unittest.TestCase):
    def test1(self):
        graph:Dict[str, List[str]] = {
            "d":["a", "b"],
            "b":["f"], 
            "a":["f"],
            "c":["d"]
        }
        expected:List[str] = ["f", "e", "a", "b", "d", "c"]
        self.assertEqual(calExecutionOrder(graph=graph), expected)

if __name__ == "__main__":
    unittest.main()