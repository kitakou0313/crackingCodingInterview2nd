from libs.linkedList import SingleLinkedList
import unittest

def getKthNodeValue(lList:SingleLinkedList, k:int):
    """
    lListの後ろからk番目の要素を返す
    """
    return True

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
            #self.assertEqual(lList.getValues(), expected)


if __name__ == "__main__":
    unittest.main()
