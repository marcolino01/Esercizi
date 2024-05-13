class Animal:
    def __init__(self, name : str, age : int):
        self.set_name : str = name
        self.set_age : int = age

        
    def get_name (self)-> str:
        return self.name
    
    def get_age (self)-> int:
        return self.age
    
    def set_name (self, new_name: str):
        self.name = new_name

    def set_age (self, new_age : int):
        self.age = new_age

    def __str__(self) -> str:
        return f'Animal(name= {self.name}, age {self.age})'
    
    def talk(self) -> str:
        return "Non so come si parla.."


class Person(Animal):
        

    def talk(self)-> str:
        return f'ciao mi chiamo {self.name}'
    
    def __add__(self, other):
        return Person(name=self.name + other.name, age=self.age + other.age)
    
        
    def __eq__(self,other)->bool:
         return self.name== other.name

    
class Studente(Person):
    def __init__(self, name: str, age: int, id : int):
        super().__init__(name, age)
        self.id = id

    def talk(self)-> str:
        s = super().talk
        return s + f'ciao mi chiamo {self.name}, e ho {self.age} anni'
    
    def bella (self, new)-> str:
        super().set_age(new)
    
    def set_age(self, new_age):
        self.age = new_age *2

    

    


a = Animal(name="bardh", age=28)
print(a.talk())
p = Person(name="Walter", age=33)
print(p)
print(p.talk)
s = Studente(name="Christian", age = 26)
print(s.name)