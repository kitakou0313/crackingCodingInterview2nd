import unittest


def isSpecific(inputtedStr):
    appearedChars = set()

    for char in inputtedStr:
        if char in appearedChars:
            return False
        appearedChars.add(char)

    return True

def isSpecificWithoutOtherDataStructure(inputtedStr):
    sortedStr = sorted(inputtedStr)

    for i in range(len(sortedStr) - 1):
        if sortedStr[i] == sortedStr[i + 1]:
            return False
    
    return True
        


class Test(unittest.TestCase):
    def test_isSpecific(self):
        self.assertEqual(isSpecific("abcdefg"), True)
        self.assertEqual(isSpecific("aaaaaa"), False)
        self.assertEqual(isSpecific(""), True)

    def test_isSpecificOtherDataStructure(self):
        self.assertEqual(isSpecificWithoutOtherDataStructure("abcdefg"), True)
        self.assertEqual(isSpecificWithoutOtherDataStructure("aaaaaa"), False)
        self.assertEqual(isSpecificWithoutOtherDataStructure(""), True)

if __name__ == "__main__":
    unittest.main()
