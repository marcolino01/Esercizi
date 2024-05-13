class Person:

    def __init__(self, cf :str, name : str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.cf = cf
        self.age = age

class Student(Person):

    def __init__(self,id :int, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.id = id