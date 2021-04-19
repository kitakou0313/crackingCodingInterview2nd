from libs.linkedList import LinkedList
import unittest

def removeDupNode(lList:LinkedList):
    """
    連結リストの重複Nodeを排除 O(len(lList))
    """
    appearedVals = set()

    for node in lList:
        if node.val in appearedVals:
            lList.removeNode(node)
        else:
            appearedVals.add(node.val)
    

class Test(unittest.TestCase):
    testCases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
    )

    def test1(self, ):
        """
        test
        """
        for test, expected in self.testCases:
            lList = LinkedList(test)
            self.assertEqual(lList.getValues(), test)

            removeDupNode(lList)

            self.assertEqual(lList.getValues(), expected)


if __name__ == "__main__":
    unittest.main()