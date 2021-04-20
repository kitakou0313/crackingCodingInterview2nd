from libs.linkedList import SingleLinkedList
import unittest

def getKthNodeValue(lList:SingleLinkedList, k:int)->int:
    """
    lListの後ろからk番目の要素を返す
    """
    runner = current = lList.head

    for _ in range(k):
        runner = runner.next

    while runner is not None:
        runner = runner.next
        current = current.next
    
    return current.val

class Test(unittest.TestCase):
    testCases = (
        ([10, 20, 30, 40, 50], 1, 50),
        ([10, 20, 30, 40, 50], 5, 10),
    )
    def test1(self, ):
        """
        test
        """
        for listVals, k , expected in self.testCases:
            lList = SingleLinkedList(list(listVals))

            self.assertEqual(lList.getValues(), listVals)
            self.assertEqual(getKthNodeValue(lList, k), expected)


if __name__ == "__main__":
    unittest.main()
