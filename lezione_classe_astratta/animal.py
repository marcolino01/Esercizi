from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name: str, age : int) -> None:
        super().__init__() 
        self.name : str = name
        self.age : int = age

    @abstractmethod
    def verso(self):
        pass 


class Cat(Animal):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def verso(self):
        print("Miao")


class Dog(Animal):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def verso(self):
        print("Bau")

class Horse(Animal):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def verso(self):
        print("HYHYYYHYHY")

dog : Dog = Dog("Fido", 2)
dog.verso()

horse : Horse = Horse("cavallo", 12)
horse.verso()
