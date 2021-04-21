from libs.linkedList import SingleLinkedList, LinkedListNode
import unittest

def removeNode(lList:SingleLinkedList,node:LinkedListNode):
    """
    与えられたリストのNodeを削除
    """
    
    node.val = node.next.val
    node.next = node.next.next
    

class Test(unittest.TestCase):
    testCases = (
        ([10, 20, 30, 40, 50], 2, [10, 20, 40, 50]),
    )
    def test1(self, ):
        """
        test
        """
        for listVals, nodeValueInd , expected in self.testCases:
            lList = SingleLinkedList((listVals[:nodeValueInd]))
            
            lList.add(listVals[nodeValueInd])
            middleNode = lList.tail
        
            lList.addMultiNode(listVals[nodeValueInd+1:])

            self.assertEqual(lList.getValues(), listVals)
            removeNode(lList, middleNode)
            self.assertEqual(lList.getValues(), expected)


if __name__ == "__main__":
    unittest.main()