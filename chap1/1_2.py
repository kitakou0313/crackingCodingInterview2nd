import unittest

def sortString(strInput):
    sortedTmp = sorted(strInput)
    res = ""

    for char in sortedTmp:
        res += char
    
    return res

#O(log min(len(str1), len(str2)))
def isPermutaition(str1, str2):
    sortedStr1 = sortString(str1)
    sortedStr2 = sortString(str2)

    return (sortedStr1 == sortedStr2)

class Test(unittest.TestCase):
    def test_isPermutation(self):
        self.assertEqual(isPermutaition("abc", "cab"), True)
        self.assertEqual(isPermutaition("abc", "def"), False)
        self.assertEqual(isPermutaition("", "abc"), False)

if __name__ == "__main__":
    unittest.main()