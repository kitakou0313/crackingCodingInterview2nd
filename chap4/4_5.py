import unittest
from libs.tree import TreeNode

# 部分木もBSTなので、葉ノードからさかのぼって最小値最大値を返す関数を作って比較すれば良さそう
def isBST(root:TreeNode) -> bool:
    return True

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