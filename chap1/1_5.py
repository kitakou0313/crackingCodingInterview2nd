import unittest

def isOneStep(str1, str2):
    if abs(len(str1)- len(str2)) > 1:
        return False

    longer = str1 if len(str1) > len(str2) else str2
    shorter = str2 if len(str1) > len(str2) else str1

    appearedChars = set()

    for char in longer:
        appearedChars.add(char)

    for char in shorter:
        if char in appearedChars:
            appearedChars.remove(char)

    if len(appearedChars) > 1:
        return False
    else:
        return True

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isOneStep("pale", "ple"), True)
        self.assertEqual(isOneStep("pales", "pale"), True)
        self.assertEqual(isOneStep("pale", "pales"), True)
        self.assertEqual(isOneStep("pale", "bale"), True)
        self.assertEqual(isOneStep("pale", "bake"), False)
        self.assertEqual(isOneStep("test", "te"), False)

        self.assertEqual(isOneStep("ale", "ele"), False)

if __name__ == "__main__":
    unittest.main()