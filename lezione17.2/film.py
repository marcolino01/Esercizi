from abc import(ABC, abstractmethod)


class Film(ABC):

    def __init__(self,codice_identificativo : int, titolo: str):
        self.codice_identificativo : int = codice_identificativo
        self.titolo : str = titolo

    def setId(self,id : int):
        self.codice_identificativo : int = id

    def setTitle(self, title: str):
        self.titolo : str = title

    def getId(self):
        return self.codice_identificativo
    
    def getTitle(self):
        return self.titolo
    
    def isEqual(self, otherfilm : 'Film'):
        if self.codice_identificativo == otherfilm.getId():
            return True
        else:
            return False
        
    @abstractmethod

    def calcolaPenaleRitardo(self):
        pass
        

