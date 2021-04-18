

class LinkedListNode(object):
    """
    連結リストのノード
    """
    def __init__(self, val, nextNode=None, prevNode=None):
        """
        コンストラクタ
        """
        self.prev = prevNode
        self.next = nextNode
        self.val = val

class LinkedList(object):
    """
    連結リスト
    """
    def __init__(self, values=None):
        """
        コンストラクタ、valuesに配列を渡すとそれらを連結リスト化
        """
        self.head = None
        self.tail = None

        if values is not None:
            for val in values:
                self.add(val)

    def add(self, value):
        """
        配列を末尾に追加
        """
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next



