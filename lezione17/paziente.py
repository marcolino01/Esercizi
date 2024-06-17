from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, codice_identificativo: str):
        super().__init__(first_name, last_name)
        self.__codice_identificativo : str = codice_identificativo
       

    def setIdCode(self, codice_identificativo : str):
        self.__codice_identificativo = codice_identificativo
        return self.__codice_identificativo
    
    def getIdCode(self):
        return self.__codice_identificativo
    
    def patientInfo(self):
        print(f"Paziente {self.getName()} {self.getLastname()}, ID : {self.getIdCode()}")
    

paz = Paziente("Mario", "Rossi", "fghj")
paz.patientInfo()