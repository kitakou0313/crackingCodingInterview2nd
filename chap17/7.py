from typing import Dict, List, Set, Tuple
import unittest
from unittest.case import TestCase
from libs.queue import StrQueue

def solver(nameAndFreq:List[tuple], synonyms:List[tuple]) -> Dict[str, int]:
    """
    シノニムの関係のグラフ構築
    各名前について
    １．結果用の辞書型の各名前のシノニムに含まれるか検索
    ２．すでにシノニムが存在していれば可算、なければ辞書に追加
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

    def findAllSynonym(name:str, synonymGraph:Dict[str, Set[str]]) -> Set[str]:
        """
        nameのシノニムを幅探してすべて返す
        """
        synonymSet:Set[str] = set()

        queue = StrQueue()
        isVisited:Set[str] = set()

        queue.push(name)
        isVisited.add(name)

        while not(queue.isEmpty()):
            nowName = queue.pop()
            for nxtName in synonymGraph[nowName]:
                if nxtName not in isVisited:
                    synonymSet.add(nxtName)
                    queue.push(nxtName)
                    isVisited.add(nxtName)

        return synonymSet

    synonymGraph = createSynonymGraph(synonyms)

    ansMap:Dict[str, int] = {}
    keyAndSynonymsMap:Dict[str, Set[str]] = {}

    for name, freq in nameAndFreq:
        isSynonym = False
        synonymName = ""
        
        for addedName in keyAndSynonymsMap:
            if name in keyAndSynonymsMap[addedName]:
                isSynonym = True
                synonymName = addedName
        
        if isSynonym:
            ansMap[synonymName] += freq
        else:
            ansMap[name] = freq
            keyAndSynonymsMap[name] = findAllSynonym(name, synonymGraph)
        

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