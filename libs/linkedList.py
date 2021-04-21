import collections

class LinkedListNode(object):
    """
    連結リストのノード
    """
    def __init__(self, val:int, nextNode=None, prevNode=None):
        """
        コンストラクタ
        """
        self.prev = prevNode
        self.next = nextNode
        self.val = val

class SingleLinkedList(object):
    """
    単方向連結リスト
    """
    def __init__(self, values:collections.abc.Iterable):
        """
        コンストラクタ、valueで配列を渡すとそれを連結リスト化
        """
        self.head = None
        self.tail = None

        for val in values:
            self.add(val)
    
    def add(self, value:any):
        """
        末尾にノードを追加
        """
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next

    def getValues(self) -> []:
        """
        全要素を配列化して返却
        """
        crtNode = self.head
        res = []
        while crtNode is not None:
            res.append(crtNode.val)
            crtNode = crtNode.next
        return res

    def addMultiNode(self, values:[]):
        """
        valueに対応するNodeを追加
        """
        for value in values:
            self.add(value)

class LinkedList(object):
    """
    双方向連結リスト
    """
    def __init__(self, values:collections.abc.Iterable):
        """
        コンストラクタ、valuesに配列を渡すとそれらを連結リスト化
        """
        self.head = None
        self.tail = None
        for val in values:
            self.add(val)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def add(self, value):
        """
        配列を末尾に追加
        """
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, nextNode=None, prevNode=self.tail)
            self.tail = self.tail.next

    def removeNode(self, node:LinkedListNode):
        """
        nodeをリストから削除
        """
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


    def getValues(self) -> []:
        """
        全ノードのvalを配列にして返却
        """
        res = []

        crtNode = self.head

        while crtNode is not None:
            res.append(crtNode.val)
            crtNode = crtNode.next

        return res


