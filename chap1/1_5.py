import unittest


def isOneStepReplace(str1, str2):
    """
    文字一つ置き換えで等しくできるか判定
    """
    flag = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if flag:
                return False
            flag = True
    return True
    
def isOneStepInsert(longer, shorter):
    """
    shorter文字列に1つ追加して等しくできるか検証
    """
    indInLonger = 0
    indInShorter = 0
    flag = False

    while indInLonger < len(longer) and indInShorter < len(shorter):
        if longer[indInLonger] != shorter[indInShorter]:
            if flag:
                return False
            flag = True
            indInLonger += 1
        else:
            indInLonger += 1
            indInShorter += 1
    return True

def isOneStep(str1, str2):
    if abs(len(str1)- len(str2)) > 1:
        return False

    longer = str1 if len(str1) > len(str2) else str2
    shorter = str2 if len(str1) > len(str2) else str1

    if len(longer) == len(shorter):
        return isOneStepReplace(longer, shorter)
    else:
        return isOneStepInsert(longer, shorter)
        


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isOneStep("pale", "ple"), True)
        self.assertEqual(isOneStep("pales", "pale"), True)
        self.assertEqual(isOneStep("pale", "pales"), True)
        self.assertEqual(isOneStep("pale", "bale"), True)
        self.assertEqual(isOneStep("pale", "bake"), False)
        self.assertEqual(isOneStep("test", "te"), False)

        self.assertEqual(isOneStep("ale", "ela"), False)

if __name__ == "__main__":
    unittest.main()