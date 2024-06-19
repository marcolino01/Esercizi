from film import Film

class Azione(Film):

    def __init__(self, codice_identificativo: int, titolo: str):
        super().__init__(codice_identificativo, titolo)
        self.__genere : str = "Azione"
        self.__penale : float = 3.0

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo : float):
        if giorniRitardo > 0:
            penaleRitardo = self.__penale * giorniRitardo
            return penaleRitardo
        else:
            pass
    
class Commedia(Film):

    def __init__(self, codice_identificativo: int, titolo: str):
        super().__init__(codice_identificativo, titolo)
        self.__genere : str = "Commedia"
        self.__penale : float = 2.5

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo: float):
        if giorniRitardo > 0:
            penaleRitardo : float = self.__penale * giorniRitardo
            return penaleRitardo
        else : 
            pass

class Dramma(Film):

    def __init__(self, codice_identificativo: int, titolo: str):
        super().__init__(codice_identificativo, titolo)
        self.__genere : str = "Drammatico"
        self.__penale : float = 2.0
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo: float):
        if giorniRitardo > 0:
            penaleRitardo: float = self.__penale * giorniRitardo
            return penaleRitardo
        else: 
            pass
        
        

       