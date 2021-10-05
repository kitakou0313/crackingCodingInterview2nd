from typing import List
import unittest

def findMajorityInArray(array:List[int]) -> int:
    """
    docstring
    """
    pass

class Test(unittest.TestCase):
    """
    docstring
    """
    def test(self):
        """
        docstring
        """
        testCases = [
            ([1,2,5,9,5,9,5,5,5], 5)
        ]

        for input, expected in testCases:
            self.assertEqual(findMajorityInArray(input), expected)

if __name__ == "__main__":
    unittest.main()