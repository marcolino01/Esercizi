from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization : str, parcel: float):
        super().__init__(first_name, last_name)
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def setSpecialization(self, specialization: str):
        if type(specialization) != str:
            return "La specializzazione inserita non è una stringa"
        else:
            self.__specialization = specialization
            return self.__specialization
        
    def setParcel(self, parcel : float):
        if type(parcel) != float:
            return "La parcella inserita non è un float!"
        else:
            self.__parcel = parcel
            return self.__parcel
    
    def getParcel(self):
        return self.__parcel
    
    def getSpecialization(self):
        return self.__specialization
    
    def isAValidDoctor(self):
        if self.getAge() > 30:
            print(f"doctor {self.getName()} {self.getLastname()} is valid")
            return True
        else:
            print(f"doctor {self.getName()} {self.getLastname()} is not valid")
            return False

    def doctorGreet(self):
        print(self.greet())
        print(f"Sono medico {self.getSpecialization()}")

doc = Dottore("ddd","ccc","www", 44.4)
doc.setAge(31)
doc.doctorGreet()
doc.isAValidDoctor()
doc.setParcel(23)
print(doc.getParcel())