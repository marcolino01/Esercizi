
import unittest
from esercizi_testi_digitali import Documento, Email, File


class TestDocumento(unittest.TestCase):

    def testDocumento(self):
        testo : Documento = Documento("Ciao Bob, possiamo incontrarci domani?")
        self.assertEqual(testo.getText(), "Ciao Bob, possiamo incontrarci domani?", "OK")
        testo.setText("Ciao")
        self.assertEqual(testo.getText(), "Ciao", "Ok")

class TestEmail(unittest.TestCase):

    def testEmail(self):
        testo : Email = Email("alice@example.com", "bob@example.com", "Incontro", "Ciao Bob, possiamo incontrarci domani?")
        self.assertEqual(testo.getText(),f"Da: {testo.getMittente()}, A: {testo.getDestinatario()} Titolo: {testo.getTitolo()} Ciao Bob, possiamo incontrarci domani?", "oook")
        self.assertEqual(testo.writeToFile("email.txt"), "email", "okk")
        with open("email.txt", "r") as doc:
            return doc.read()
        self.assertEqual(testo.isInText("incontrarci"), True, "Dajeee")


"""class TestFile(unittest.TestCase):

    def testFile(self):
        testo : File = File("document.txt")
        self.assertEqual(testo.getText(), , "oookk")
        self.assertEqual(testo.isInText(), testo, "ooook")"""


if __name__ == "__main__":

    unittest.main()