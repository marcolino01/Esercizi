class Documento:

    def __init__(self, testo: str)-> None:
        self.testo : str = testo

    def getText(self)-> str:
        return self.testo
    
    def setText(self, testo1: str)-> None:
        self.testo : str = testo1

    def isInText(self, parola_chiave: str)-> bool:
        
        if parola_chiave in self.getText():
            return True
        else :
            return False
        
class Email(Documento):

    def __init__(self, mittente: str, destinatario: str, titolo: str, testo: str) -> None:
        super().__init__(testo)
        self.mittente : str = mittente
        self.destinatario : str = destinatario
        self.titolo : str = titolo

    def getMittente(self) ->str:
        return self.mittente
    
    def setMittente(self, mittente1: str)-> None:
        self.mittente : str = mittente1

    def getDestinatario(self)-> str:
        return self.destinatario

    def setDestinatario(self, destinatario1 : str)-> None:
        self.destinatario : str = destinatario1

    def getTitolo(self)-> str:
        return self.titolo    

    def getText(self)-> str:
        s : str = ""
        s += f"Da: {self.getMittente()}, A: {self.getDestinatario()}"
        s += f" Titolo: {self.getTitolo()} " 
        s+= self.testo 
        return s       

    def writeToFile(self, nome_file : str)-> str:
        with open(nome_file, 'w') as doc:
            return doc.write(self.testo)


class File(Documento):

    def __init__(self, nomePercorso: str) -> None:
        self.nomePercorso : str = nomePercorso

    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as doc:
            return doc.read()
    
    def getText(self)-> str:
        s : str = ""
        s += f"Percorso : {self.nomePercorso}"
        s += f" Contenuto: {self.leggiTestoDaFile()}"
        return s


    
"""email : Email = Email("marco", "sss", "lista", "Ciao Bob, possiamo incontrarci domani?")
file : File = File("document.txt")
print(email.getText())
print(file.getText())
email.writeToFile("email.txt")
print(email.isInText("incontrarci"))
print(email.isInText("percorso"))"""