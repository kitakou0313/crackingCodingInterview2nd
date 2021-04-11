import unittest

def sortString(strInput):
    sortedTmp = sorted(strInput)
    res = ""

    for char in sortedTmp:
        res += char
    
    return res

#O(log max(len(str1), len(str2)))
def isPermutaition(str1, str2):
    sortedStr1 = sortString(str1)
    sortedStr2 = sortString(str2)

    return (sortedStr1 == sortedStr2)

# O(max(len(str1), len(str2)))
def isPermutaition2(str1, str2):
    if len(str1) != len(str2):
        return False

    charAndNumOfEncounters = {}

    for char in str1:
        if char not in charAndNumOfEncounters:
            charAndNumOfEncounters[char] = 0

        charAndNumOfEncounters[char] += 1

    for char in str2:
        if char not in charAndNumOfEncounters:
            return False
        
        charAndNumOfEncounters[char] -= 1

        if charAndNumOfEncounters[char] < 0:
            return False

    for char, numOfEncounters in charAndNumOfEncounters.items():
        if numOfEncounters != 0:
            return False

    return True


    

class Test(unittest.TestCase):
    def test_isPermutation(self):
        self.assertEqual(isPermutaition("abc", "cab"), True)
        self.assertEqual(isPermutaition("abc", "def"), False)
        self.assertEqual(isPermutaition("", "abc"), False)

    def test_isPermutation2(self):
        self.assertEqual(isPermutaition2("abc", "cab"), True)
        self.assertEqual(isPermutaition2("abc", "def"), False)
        self.assertEqual(isPermutaition2("", "abc"), False)
        self.assertEqual(isPermutaition2("ttttt", "abc"), False)


if __name__ == "__main__":
    unittest.main()