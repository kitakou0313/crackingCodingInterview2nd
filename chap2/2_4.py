from libs.linkedList import SingleLinkedList, LinkedListNode
import unittest

def splitListWithK(lList:SingleLinkedList, K:int) -> None:
    """
    単方向連結リストをKのvalueを持つノードで分割して並び替え
    """
    current:LinkedListNode = lList.head 
    newHead:LinkedListNode = lList.head
    newTail:LinkedListNode = lList.head

    while current is not None:
        nextNode = current.next
        current.next = None

        if current.val < K:
            current.next = newHead
            newHead = current
        else:
            newTail.next = current
            newTail = current

        current = nextNode

    if newTail.next is not None:
        newTail.next = None

    lList.setTail(newTail)
    lList.setHead(newHead)

class Test(unittest.TestCase):
    testCases = (
        ([3,5,8,5,10,2,1], 5, [1, 2, 3, 5, 8, 5, 10]),
    )
    def test1(self, ):
        """
        test
        """
        for listVals, K , expected in self.testCases:
            lList = SingleLinkedList((listVals))

            self.assertEqual(lList.getValues(), listVals)
            splitListWithK(lList, K)
            self.assertEqual(lList.getValues(), expected)

if __name__ == "__main__":
    unittest.main()
    