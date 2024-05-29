"""from abc import ABC, abstractmethod

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
horse.verso()"""

from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):
        pass


class Cane(AbcAnimal):

    def __init__(self, nome: str, ):
        self.nome : str = nome

    def verso(self):
        print("Bau")

class Gatto(AbcAnimal):

    def __init__(self, nome: str, ):
        self.nome : str = nome

    def verso(self):
        print("Miao")

class Coccodrillo(AbcAnimal):

    def __init__(self, nome: str, ):
        self.nome : str = nome

    def verso(self):
        pass


cane : Cane = Cane("Pluto")
gatto : Gatto = Gatto("Tom")
coccodrillo : Coccodrillo = Coccodrillo("Giovanni")

#from typing import Any se io inserisco il typing ANY posso passare qualsiasi tipo di dati
#from typin import TypeAlisa posso crearmi un tipo chiamrlo in un modo e richiamrlo all'occorenza "tipocomposto : TypeAlias = tipo che voglio sostituire", 
#si fa quando il tipo è composto e lungo


a : dict[str, int | str] = {             # "|" sta per OR
    "key1": "val_1",
    "key2": "val_2",
    "key3": "val_3"
    }

lista_animali : list[AbcAnimal] = [cane, gatto, coccodrillo]

for i in lista_animali:
    i.verso()
