import unittest

def isPermutationOfPalindrome(inputStr):
    """
    inputStrが回文の順列かどうか判定
    """

    # deleting spaces
    inputStr = inputStr.replace(" ", "")
    # Change Upper case to Lower case
    inputStr = inputStr.lower()

    charAndNumOfEncounter = {}
    for char in inputStr:
        if not(char in charAndNumOfEncounter):
            charAndNumOfEncounter[char] = 0
        charAndNumOfEncounter[char] +=  1
    

    if len(inputStr) % 2 == 1:
        flag = False
        for _,numOfEncounter in charAndNumOfEncounter.items():
            if numOfEncounter % 2 == 1:
                if flag == True:
                    return False
                flag = True
        return True
    else:
        for _, numOfEncounter in charAndNumOfEncounter.items():
            if numOfEncounter % 2 == 1:
                return False
        
        return True
            


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isPermutationOfPalindrome("Tact Coa"), True)
        self.assertEqual(isPermutationOfPalindrome("abcde fghi"), False)
        self.assertEqual(isPermutationOfPalindrome("Able was I ere I saw Elba"), True)
        self.assertEqual(isPermutationOfPalindrome("abAB"), True)





if __name__ == "__main__":
    unittest.main()