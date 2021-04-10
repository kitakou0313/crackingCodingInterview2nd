import unittest


def isSpecific(inputtedStr):
    appearedChars = set()

    for char in inputtedStr:
        if char in appearedChars:
            return False
        appearedChars.add(char)

    return True
        


class Test(unittest.TestCase):
    def test_isSpecific(self):
        self.assertEqual(isSpecific("abcdefg"), True)
        self.assertEqual(isSpecific("aaaaaa"), False)
        self.assertEqual(isSpecific(""), True)

if __name__ == "__main__":
    unittest.main()
