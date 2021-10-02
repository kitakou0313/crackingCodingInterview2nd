from unittest import TestCase
import unittest

class Test(TestCase):
    """
    docstring
    """
    def test(self):
        """
        docstring
        """
        testCases = [
            ([(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)],6)
        ]

        for inputted, expected in testCases:
            print(inputted, expected) 

if __name__ == "__main__":
    unittest.main()