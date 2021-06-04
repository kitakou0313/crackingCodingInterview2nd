from typing import List
import unittest
import time

class Animal(object):
    """
    動物クラス
    """
    def __init__(self, name:str):
        """
        コンストラクタ
        """
        self.__name:str = name
        self.__time:float = time.time()

    def getTime(self) -> float:
        return self.__time

class Dog(Animal):
    """
    犬クラス
    """
    def __init__(self, name: str):
        super().__init__(name)
    
    

class Cat(Animal):
    """
    猫クラス
    """
    def __init__(self, name: str):
        super().__init__(name)

class AnimalQueue(object):
    """
    DogClass専用のQueue
    """
    def __init__(self):
        """
        コンストラクタ
        """
        self.__animals:List[Animal] = []

    def pop(self) -> Animal:
        """
        Pop
        """
        return self.__animals.pop(0)
    
    def push(self, animal:Animal) -> None:
        """
        Push
        """
        self.__animals.append(animal)

    def isEmpty(self) -> bool:
        """
        空か返す
        """
        return len(self.__animals) == 0
    
    def top(self) -> Animal:
        return self.__animals[0]


class AnimalShelter(object):
    """
    動物病院クラス
    """
    def __init__(self) -> None:
        self.__dogQueue:AnimalQueue = AnimalQueue()
        self.__catQueue:AnimalQueue = AnimalQueue()

    
    def enqueue(self, animal:Animal) -> None:
        if type(animal) == Dog:
            self.__dogQueue.push(animal)

        if type(animal) == Cat:
            self.__catQueue.push(animal)
    
    def dequeueCat(self) -> Animal:
        """
        Catを出す
        """
        return self.__catQueue.pop()
    
    def dequeueDog(self) -> Animal:
        """
        Dogを出す
        """
        return self.__dogQueue.pop()

    def dequeueAny(self) -> Animal:
        if self.__dogQueue.isEmpty() and self.__catQueue.isEmpty():
            return None
        
        elif not(self.__dogQueue.isEmpty()) and self.__catQueue.isEmpty():
            return self.__dogQueue.pop()

        elif self.__dogQueue.isEmpty() and not(self.__catQueue.isEmpty()):
            return self.__catQueue.pop()

        else:
            if self.__dogQueue.top().getTime() < self.__catQueue.top().getTime():
                return self.__dogQueue.pop()
            else:
                return self.__catQueue.pop()


class Test(unittest.TestCase):
    def test1(self):
        animals:List[Animal] = [Dog("Taro"), Cat("Tama"), Cat("Mikan"), Dog("Sasuke")]
        q = AnimalShelter()

        for animal in animals:
            q.enqueue(animal)

        for expected in animals:
            actual = q.dequeueAny()
            self.assertEqual(expected,actual)

    def test2(self):
        dogs:List[Dog] = [Dog("Taro"), Dog("Sasuke")]
        cats:List[Cat] = [Cat("Tama"), Cat("Mikan")]

        q = AnimalShelter()

        q.enqueue(dogs[0])
        q.enqueue(cats[0])
        q.enqueue(dogs[1])
        q.enqueue(cats[1])

        for expectedDog in dogs:
            actualDog:Dog = q.dequeueDog()
            self.assertEqual(actualDog, expectedDog)

        for expectedCat in cats:
            actualCat:Cat = q.dequeueCat()
            self.assertEqual(actualCat, expectedCat)


if __name__ == "__main__":
    unittest.main()