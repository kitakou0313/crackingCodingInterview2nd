from libs.linkedList import SingleLinkedList, LinkedListNode
import unittest

def sumTwoLinkedList(list1:SingleLinkedList, list2:SingleLinkedList) -> SingleLinkedList:
    """
    二つのリストを複数桁の数字と見なし、合計した連結リストを返す
    """
    ansList:SingleLinkedList = SingleLinkedList()

    list1.add(0)
    list2.add(0)

    currentInList1:LinkedListNode = list1.head
    currentInList2:LinkedListNode = list2.head

    carry:int = 0
    while currentInList1 is not None and currentInList2 is not None:
        res = (currentInList1.val + currentInList2.val + carry)

        ansList.add(res % 10)
        carry = res // 10

        currentInList1 = currentInList1.next
        currentInList2 = currentInList2.next

    if ansList.tail.val == 0:
        for node in ansList:
            if node.next == ansList.tail:
                ansList.tail = node
                node.next = None

    return ansList
    

class Test(unittest.TestCase):
    testCases = (
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        ([3, 2, 6], [3, 2, 5], [6, 4, 1, 1]),
        ([0], [0], [0]),
        ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    )
    def test1(self, ):
        """
        test
        """
        for list1Values, list2Values, expected in self.testCases:
            list1 = SingleLinkedList(list1Values)
            list2 = SingleLinkedList(list2Values)

            self.assertEqual(list1.getValues(), list1Values)
            self.assertEqual(list2.getValues(), list2Values)

            res = sumTwoLinkedList(list1, list2)

            self.assertEqual(res.getValues(), expected)



if __name__ == "__main__":
    unittest.main()