import unittest
import copy

def zeroIndex(matrix):
    """
    matrixに0があれば、行と列を0で埋めて返す
    """

    res = copy.deepcopy(matrix)

    M = len(matrix)

    # 0で埋める列、行のリスト
    cols = set()
    rows = set()

    for col in range(M):
        for row in range(M):
            if res[col][row] == 0:
                cols.add(col)
                rows.add(row)

    for col in cols:
        for i in range(M):
            res[col][i] = 0

    for row in rows:
        for i in range(M):
            res[i][row] = 0

    return res

class Test(unittest.TestCase):
    testCases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    def test_string_compression(self):
            for test, expected in self.testCases:
                assert zeroIndex(test) == expected


if __name__ == "__main__":
    unittest.main()