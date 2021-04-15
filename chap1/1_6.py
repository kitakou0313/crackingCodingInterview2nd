import unittest
import time

def compressionString(string):
    """
    文字列圧縮を行い、短い方を返す
    """
    if string == "":
        return ""

    compressedString = ""

    nowChar = string[0]
    numOfNowChar = 1
    for ind in range(1, len(string)):
        if nowChar != string[ind]:
            compressedString += nowChar + str(numOfNowChar)
            
            nowChar = string[ind]
            numOfNowChar = 1
        else:
            numOfNowChar += 1

    compressedString += nowChar + str(numOfNowChar)

    return compressedString if len(compressedString) < len(string) else string

class Test(unittest.TestCase):
    testCases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    def test_string_compression(self):
            for testString, expected in self.testCases:
                assert compressionString(testString) == expected


if __name__ == "__main__":
    unittest.main()