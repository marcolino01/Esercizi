class Persona:

    def __init__(self, first_name: str, last_name: str):
        
        if type(first_name) != str:
            print("il nome inserito non è una stringa")
            self.__first_name = None
        else:
            self.__first_name = first_name
        
        if type(last_name) != str:
            print("il cognome inserito non è una stringa")
            self.__last_name = None
        else:
            self.__last_name = last_name
        
        if type(last_name) == str and type(first_name) == (str):
            self.setAge(0)
        else:
            self.__age = None
        
    
    def setName(self, first_name: str):
        self.__first_name = first_name
        if type(self.__first_name) != str:
            self.__first_name = None
            return "il nome inserito non è una stringa"
        else:
            return self.__first_name

    def setLastName(self, last_name: str):
        self.__last_name = last_name
        if type(self.__last_name) != str:
            self.__last_name= None
            return "il cognome inserito non è una stringa"
        else:
            return self.__last_name

    def setAge(self, age: int):
        self.__age : int = age
        if type(self.__age) != int:
            return self.__age
        else:
            return "non è un numero intero"
        
    def getName(self):
        return self.__first_name
    
    def getLastname(self):
        return self.__last_name

    def getAge(self):
        return self.__age

    def greet(self):
        print(f"Ciao, sono {self.getName()} {self.getLastname()}! Ho {self.getAge()} anni")   

persona = Persona("nnn", "sss")
persona.setLastName("Dddd")
persona.setLastName("ccc")
persona.setAge(44)


persona.greet()


