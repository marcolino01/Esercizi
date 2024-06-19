from paziente import Paziente
from dottore import Dottore

class Fattura:

    def __init__ (self, patient: list[Paziente], doctor: Dottore):
 
        
        if doctor.isAValidDoctor():
            self.patient : list[Paziente] = patient
            self.fatture : int = len(patient)
            self.salary : int = 0
            self.doctor : Dottore = doctor
        else:
            self.patient : list[Paziente] = None
            self.fatture : int = None
            self.salary : int = None
            self.doctor : Dottore = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        if len(self.patient) > 0:
            salary : float = len(self.patient) * self.doctor.getParcel()
            return salary
        else :
            pass
    
    def getFatture(self):
        if len(self.patient) > 0:
            fatture : int = len(self.patient)
            return fatture
        else :
            pass

    def addPatient(self, newPatient: Paziente):
        if newPatient not in self.patient:
            self.patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        else: 
            pass


    def removePatient(self, idCode: str):
        if len(self.patient) > 0:
            for patie in self.patient:     #patie = paziente
                if idCode == patie.getIdCode():
                    self.patient.remove(patie)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del dottor {self.doctor.getLastname()} è stato rimosso il paziente {patie}")
                else: 
                    pass
        else:
            pass

paziente : Paziente = Paziente("Mario", "Rossi", "fghj")
paziente2 : Paziente = Paziente("Marco", "Rossi", "jjjj")
dottore : Dottore = Dottore("gino", "Gino","Chirurgia", 77.7)
dottore.setAge(45)
pazienti : list[Paziente]= [paziente, paziente2]
fattura : Fattura = Fattura(pazienti, dottore)
        


