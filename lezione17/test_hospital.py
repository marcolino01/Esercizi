import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class TestPersona(unittest.TestCase):

    def test_iniziale(self):
        persona : Persona = Persona("Mario", "Rossi")
        self.assertEqual(type(persona.getName()), str)
        self.assertEqual(type(persona.getLastname()), str)
        self.assertEqual(persona.getAge(), 0)

    def test_greet(self):
        persona: Persona = Persona("Mario", "Rossi")
        persona.setAge(5)
        self.assertEqual(persona.getName(), "Mario")
        self.assertEqual(persona.getLastname(), "Rossi")
        self.assertEqual(persona.getAge(), 5)

class TestDottore(unittest.TestCase):

    def test(self):
        dottore : Dottore = Dottore("Mario", "Rossi", "Chirurgia", 100.0)
        self.assertEqual(dottore.getName(), "Mario")
        self.assertEqual(dottore.getLastname(), "Rossi")
        self.assertEqual(dottore.getSpecialization(), "Chirurgia")
        self.assertEqual(dottore.getParcel(), 100.0)
        self.assertEqual(dottore.isAValidDoctor(), False)
        dottore.setAge(32)
        self.assertEqual(dottore.isAValidDoctor(), True)

class TestPaziente(unittest.TestCase):

    def test(self):
        paziente : Paziente = Paziente("Mario", "Rossi", "fghj")
        self.assertEqual(paziente.getIdCode(), "fghj")
    

class TestFattura(unittest.TestCase):

    def test(self):
        paziente : Paziente = Paziente("Mario", "Rossi", "fghj")
        paziente2 : Paziente = Paziente("Marco", "Rossi", "jjjj")
        dottore : Dottore = Dottore("gino", "Gino","Chirurgia", 77.7)
        dottore.setAge(45)
        fattura : Fattura = Fattura([paziente2], dottore)
        



if __name__ == "__main__":

    unittest.main()