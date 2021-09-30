from typing import Dict, List, Set, Tuple
import unittest
from unittest.case import TestCase

def solver(nameAndFreq:List[tuple], synonyms:List[tuple]) -> Dict[str, int]:
    """
    シノニムの関係のグラフ構築
    各名前について
    １．シノニムをすべて上のグラフから取得
    ２．各シノニムについてすでにシノニムが存在していれば可算、辞書に追加
    """
    def createSynonymGraph(synonyms:List[tuple]) -> Dict[str, Set[str]]:
        """
        docstring
        """
        synonymGraph:Dict[str, Set[str]] = dict()

        for synonym in synonyms:
            name1 = synonym[0]
            name2 = synonym[1]

            if name1 not in synonymGraph:
                synonymGraph[name1] = set()
            if name2 not in synonymGraph:
                synonymGraph[name2] = set()
            
            synonymGraph[name1].add(name2)
            synonymGraph[name2].add(name1)

        return synonymGraph

    synonymGraph = createSynonymGraph(synonyms)

    ansMap:Dict[str, int] = {}
    return ansMap
    pass

class Test(unittest.TestCase):
    """
    docstring
    """
    def test(self):
        """
        書籍のケース
        """
        nameAndFreq:List[tuple] = [
            ("John", 15),
            ("Jon", 12),
            ("Chris", 13),
            ("Kris", 4),
            ("Christopher", 19)
        ]

        synonyms = [
            ("Jon", "John"),
            ("John", "Johnny"),
            ("Chris", "Kris"),
            ("Chris", "Christopher")
        ]

        expected:Dict[str, int] = {
            "John":27,
            "Kris":36
        }

        self.assertEqual(solver(nameAndFreq, synonyms), expected)


if __name__ == "__main__":
    unittest.main()