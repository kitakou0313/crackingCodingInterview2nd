from typing import List, Tuple
import unittest
from unittest.main import main
from libs.tree import TreeNode

def createMinimalTree(values:List[int]) -> TreeNode:
    """
    高さが最小の二分探索木を作成
    """
    #方針:与えられる配列は常にソートされているため、2等分して常に中心の要素を根とする木を再帰的に作る
    middleInd:int = len(values) // 2
    middleVal:int = values[middleInd]

    rootNode:TreeNode = TreeNode(middleVal)

    leftTreeValues:List[int] = values[:middleInd]
    rightTreeValues:List[int] = values[middleInd+1:]

    if len(leftTreeValues) != 0:
        rootNode.setLeftNode(createMinimalTree(leftTreeValues))
    if len(rightTreeValues) != 0:
        rootNode.setRightNode(createMinimalTree(rightTreeValues))

    return rootNode
    

def calTreeHight(rootNode:TreeNode) -> int:
        """
        木の高さを返す
        """
        if rootNode is None:
            return 0
            
        leftTreeHeight:int = calTreeHight(rootNode.getLeftNode())
        rightTreeHeight:int = calTreeHight(rootNode.getRightNode())

        return 1 + max(leftTreeHeight, rightTreeHeight)

class Test(unittest.TestCase):
    
    def test1(self):
        testCases = [
            ([1,2,3], 2),
            ([1,2], 2),
            ([1,2,3,4], 3)
        ]

        for inputCase, expected in testCases:
            rootNode = createMinimalTree(inputCase)
            self.assertEqual(calTreeHight(rootNode), expected)

if __name__ == "__main__":
    unittest.main()