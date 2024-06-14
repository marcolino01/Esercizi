from paziente import Paziente
from dottore import Dottore

class Fattura:

    def init (self, patient: list[Paziente], doctor: Dottore):
 
        
        if doctor.isAValidDoctor():
            self.patient : list[Paziente] = []
            self.fatture : int = len(patient)
            self.salary : int = 0
            self.doctor : Dottore = doctor
        else:

