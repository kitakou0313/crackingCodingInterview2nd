from typing import List, Set, Tuple
import unittest


def findShortestSubArrayIncludingElements(elements: Set[int], array: List[int]) -> Tuple[int]:
    """
    arrayの中からelements内の要素すべてを持つ最短の部分配列を探索、インデックスを返す
    brute force...O(n^2) 各インデックスに対して先頭から末尾まで探索、elementsをすべて含めば記録

    改善策…尺取り法使えそう
    全部含むまで進める、含んだら頭進める
    O(n)?
    """
    # len(array) + 1の長さはありえないため

    # for startInd in range(len(array)):
    #     elementsMustIncluded = set(elements)

    #     for endInd in range(startInd, len(array)):
    #         if array[endInd] in elementsMustIncluded:
    #             elementsMustIncluded.remove(array[endInd])

    #         if len(elementsMustIncluded) == 0:
    #             if (endInd - startInd + 1) < (shortestSubArrayEndInd - shortestSubArrayStartInd + 1):
    #                 shortestSubArrayStartInd = startInd
    #                 shortestSubArrayEndInd = endInd
    #             break

    shortestSubArrayStartInd = -1
    shortestSubArrayEndInd = len(array)

    right = 0
    elementsIncludedInSubArray: Set[int] = set()

    for left in range(len(array)):
        while (right < len(array) and not(elementsIncludedInSubArray.issuperset(elements))):
            elementsIncludedInSubArray.add(array[right])
            right += 1

        if elementsIncludedInSubArray.issuperset(elements):
            if (shortestSubArrayEndInd - shortestSubArrayStartInd + 1) > right - left:
                shortestSubArrayStartInd = left
                shortestSubArrayEndInd = right - 1

        if right == left:
            right += 1
        else:
            elementsIncludedInSubArray.discard(array[left])

    return (shortestSubArrayStartInd, shortestSubArrayEndInd)


class Test(unittest.TestCase):
    """
    docstring
    """

    def test(self):
        """
        docstring
        """
        testCase = [
            (set([1, 5, 9]), [7, 5, 9, 0, 2, 1, 3,
             5, 7, 9, 1, 1, 5, 8, 8, 9, 7], (7, 10))
        ]

        for elements, array, expected in testCase:
            self.assertEqual(findShortestSubArrayIncludingElements(
                elements, array), expected)


if __name__ == "__main__":
    unittest.main()
