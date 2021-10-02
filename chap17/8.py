from typing import Tuple, List
from unittest import TestCase
import unittest

def calMaxTowerHeight(peopleList:List[Tuple[int]]) -> int:
    """
    docstring
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