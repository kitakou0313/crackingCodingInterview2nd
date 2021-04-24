from libs.linkedList import SingleLinkedList
import unittest

def sumTwoLinkedList(list1:SingleLinkedList, list2:SingleLinkedList) -> SingleLinkedList:
    """
    二つのリストを複数桁の数字と見なし、合計した連結リストを返す
    """

    ansList = SingleLinkedList()



    return ansList
    

class Test(unittest.TestCase):
    testCases = (
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        ([0], [0], [0]),
        ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
        ([123], [123], [246]),
        ([123], [1], [124]),
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



if __name__ == "__main__":
    unittest.main()