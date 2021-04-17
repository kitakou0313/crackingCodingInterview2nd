import unittest

def isSubString(strA, strB):
    """
    strAがstrBの部分文字列か判定
    """
    return strA in strB

def isStringRotation(str1, str2):
    """
    str2がstr1の回転であるか調べる
    """

    if len(str1) != len(str2):
        return False

    return isSubString(str2, str1+str1)

class Test(unittest.TestCase):
    testCases =[
        (("waterbottle", "erbottlewat"), True),
        (("foo", "bar"), False),
        (("foo", "foofoo"), False),
    ]
    def test(self):
            for test, expected in self.testCases:
                assert isStringRotation(*test) == expected


if __name__ == "__main__":
    unittest.main()