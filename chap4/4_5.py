from typing import Tuple
import unittest
from libs.tree import TreeNode

# 部分木もBSTなので、葉ノードからさかのぼって最小値最大値を返す関数を作って比較すれば良さそう

class MinAndMaxValAndIsBST():
    """
    下の木の最大値、最小値、BSTかどうかの探索結果
    """
    def __init__(self, minVal:int, maxVal:int, isBST:bool) -> None:
        self.min = minVal
        self.max = maxVal
        self.isBST = isBST

def searchMinAndMaxVal(root:TreeNode) -> MinAndMaxValAndIsBST:
    if (root.getLeftNode() is None) and (root.getRightNode() is None):
        return MinAndMaxValAndIsBST(root.getVal(), root.getVal(), True)

    leftNodeRes = MinAndMaxValAndIsBST(0, -float("inf"), True)
    if not(root.getLeftNode() is None):
        leftNodeRes = searchMinAndMaxVal(root.getLeftNode())

    rightNodeRes = MinAndMaxValAndIsBST(float("inf"), 0, True)
    if not(root.getRightNode() is None):
        rightNodeRes = searchMinAndMaxVal(root.getRightNode())

    if not(leftNodeRes.isBST) or not(rightNodeRes.isBST):
        return MinAndMaxValAndIsBST(0,0,False)

    if leftNodeRes.max < root.getVal():
        return MinAndMaxValAndIsBST(0,0,False)
    
    if rightNodeRes.min > root.getVal():
        return MinAndMaxValAndIsBST(0,0,False)

    return MinAndMaxValAndIsBST(leftNodeRes.min, rightNodeRes.max, True)

def isBST(root:TreeNode) -> bool:
    rootNodeRes = searchMinAndMaxVal(root)
    return rootNodeRes.isBST

class Test(unittest.TestCase):
    """
    docstring
    """
    def Test1(self):
        """
        単体テスト
        """


if __name__ == "__main__":
    unittest.main()