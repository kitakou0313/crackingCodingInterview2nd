from libs.linkedList import SingleLinkedList, LinkedListNode
from libs.stack import IntStack
import unittest

def isKaibunList(lList:SingleLinkedList) -> bool:

    stack = IntStack()
    length = lList.calLength()

    currentNode:LinkedListNode = lList.head

    for _ in range(length // 2):
            stack.add(currentNode.val)
            currentNode = currentNode.next
    
    if length % 2 == 1:
        currentNode = currentNode.next

    for _ in range(length // 2):
        if currentNode.val != stack.getTop():
            return False
        else:
            stack.pop()
            currentNode = currentNode.next
            
    return True

class Test(unittest.TestCase):
    testCases = (
        ([1], True),
        ([2,3,5,3,2], True),
        ([2,2,5,2,2], True),
        ([4,1,1,4], True),
        ([5,4,3,1],False),
        ([5,4,1],False),
    )
    def test1(self, ):
        """
        test
        """
        for testInput, expected in self.testCases:
            lList = SingleLinkedList(testInput)
            self.assertEqual(lList.getValues(), testInput)

            self.assertEqual(isKaibunList(lList), expected)


if __name__ == "__main__":
    unittest.main()