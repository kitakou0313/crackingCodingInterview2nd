class TreeNode(object):
    """
    Int型を要素に持つ木のNode
    """
    def __init__(self, val:int) -> None:
        super().__init__()
        self.__val:int = val
        self.__left:TreeNode = None
        self.__right:TreeNode = None

    def getVal(self) -> int:
        """
        Val返却
        """
        return self.__val

    def setLeftNode(self, node:'TreeNode') -> None:
        """
        左Nodeをセット
        """
        self.__left = node

    def getLeftNode(self) -> 'TreeNode':
        """
        左Nodeを取得
        """
        return self.__left

    
    def setRightNode(self, node:'TreeNode') -> None:
        """
        右Nodeをセット
        """
        self.__right = node

    def getRightNode(self) -> 'TreeNode':
        """
        右Node取得
        """
        return self.__right        