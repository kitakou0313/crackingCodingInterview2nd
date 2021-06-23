import unittest

def fillMapWithColor(map, pos, color):
    pass

class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            ([
                [0,1,1,1,1,1,0],
                [0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0],
                [0,1,1,1,1,1,0],
            ], (2,3), 1, 
            [
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
            ]
            )
        ]

        for [oriMap, pos, color, expected] in testCases:
            self.assertEqual(fillMapWithColor(oriMap, pos, color), expected)


if __name__ == "__main__":
    unittest.main()