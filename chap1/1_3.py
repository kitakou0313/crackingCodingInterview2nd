import unittest

def URLify(inputStr, length):
    """
    inputStrの空白文字列を%20に変換する
    """
    spaceURLified = "%20"
    numOfSpaces = 0

    for char in inputStr:
        if char == " ":
            numOfSpaces += 1

    StringURLified = [" " for _ in range(length - numOfSpaces + (numOfSpaces) * len(spaceURLified) )]

    indOfStringURLified = len(StringURLified)-1

    for indInInputString in range(len(inputStr)-1, -1, -1):
        if inputStr[indInInputString] != " ":
            StringURLified[indOfStringURLified] = inputStr[indInInputString]
            indOfStringURLified -= 1
        else:
            StringURLified[indOfStringURLified] = spaceURLified[2]
            StringURLified[indOfStringURLified-1] = spaceURLified[1]
            StringURLified[indOfStringURLified-2] = spaceURLified[0]

            indOfStringURLified -= 3

    return "".join(StringURLified)
    

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(URLify("Mr John Smith", 13), "Mr%20John%20Smith")
        self.assertEqual(URLify("much ado about nothing", 22), 'much%20ado%20about%20nothing')



if __name__ == "__main__":
    unittest.main()