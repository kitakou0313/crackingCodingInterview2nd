from libs.linkedList import LinkedList
import unittest

def isHavingLoop(ll:LinkedList) -> bool:
    """
    Linked Listのループ検知
    時間O(n)
    空間O(n)
    """
    isAppeared = set()

    for node in ll:
        if node in isAppeared:
            return True
        isAppeared.add(node)

    return False

class Test(unittest.TestCase):
    def test1(self, ):
        """
        test
        """
        testCases = (
            (True, True),
            (False, False)
        )
        for isLoop, expected in testCases:
            ll = LinkedList([1,2,3,4,5])

            if isLoop:
                ll.tail.next = ll.head

            self.assertEqual(isHavingLoop(ll),expected)

if __name__ == "__main__":
    unittest.main()