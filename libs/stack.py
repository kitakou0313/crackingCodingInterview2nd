import copy

class IntStack(object):
    """
    int用Stack
    """
    def __init__(self):
        """
        コンストラクタ
        """
        self.data:[int] =[]

    def pop(self) -> int:
        """
        出す
        """
        return self.data.pop()
    
    def add(self, value:int) -> None:
        """
        入れる
        """
        self.data.append(value)

    def isEmpty(self) -> bool:
        """
        要素なしか返す
        """
        return len(self.data) == 0

    def len(self) -> int:
        """
        長さ返却
        """
        return len(self.data)

    def getTop(self) -> int:
        """
        スタックの頂点要素を返す
        """
        return self.data[-1]
        
        