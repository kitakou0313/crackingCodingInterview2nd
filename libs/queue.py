import unittest
from typing import List


class IntQueue():
    """
    int用Queue
    """
    def __init__(self):
        """
        コンストラクタ
        """
        self.__data:List[int] = []

    def pop(self) -> int:
        """
        ポップ
        """
        return self.__data.pop(0)

    def push(self, value:int) -> None:
        """
        追加
        """
        self.__data.append(value)

    def isEmpty(self) -> bool:
        """
        空か判定
        """
        return len(self.__data) == 0


class StrQueue():
    """
    int用Queue
    """
    def __init__(self):
        """
        コンストラクタ
        """
        self.__data:List[str] = []

    def pop(self) -> str:
        """
        ポップ
        """
        return self.__data.pop(0)

    def push(self, value:str) -> None:
        """
        追加
        """
        self.__data.append(value)

    def isEmpty(self) -> bool:
        """
        空か判定
        """
        return len(self.__data) == 0


class Test(unittest.TestCase):
    def test1(self):
        q = IntQueue()

        datas = [1,2,3,4,5,6,7,8,9]
        for val in datas:
            q.push(val)

        for val in datas:
            num = q.pop()
            self.assertEqual(num, val)

if __name__ == "__main__":
    unittest.main()