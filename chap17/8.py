from typing import Tuple, List
from unittest import TestCase
import unittest

def calMaxTowerHeight(peopleList:List[Tuple[int]]) -> int:
    """
    全順序、全選び方について探索 O(2^n * nCn)
    """
    pass

class Test(TestCase):
    """
    docstring
    """
    def test(self):
        """
        docstring
        """
        testCases = [
            ([(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)],6)
        ]

        for inputtedCase, expected in testCases:
            self.assertEqual(calMaxTowerHeight(inputtedCase), expected)

if __name__ == "__main__":
    unittest.main()