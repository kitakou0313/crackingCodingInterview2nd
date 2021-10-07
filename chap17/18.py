from typing import List, Set, Tuple
import unittest

def findShortestSubArrayIncludingElements(elements:Set[int], array:List[int]) -> Tuple[int]:
    """
    arrayの中からelements内の要素すべてを持つ最短の部分配列を探索、インデックスを返す
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
        testCase = [
            (set([1,5,9]), [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7], (7,10))
        ]

        for elements, array, expected in testCase:
            self.assertEqual(findShortestSubArrayIncludingElements(elements, array),expected)

if __name__ == "__main__":
    unittest.main()