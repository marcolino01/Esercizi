from abc import (ABC,abstractmethod)
import string


class CodificatoreMessagio(ABC):

    @abstractmethod
    def codifica(self,testoInChiaro: str)-> str:
        pass

class DecodificatoreMessaggio(ABC):        
    @abstractmethod
    def decodifica(self,testoCodificato: str)->str:
        pass
    
class CifratoreAScorrimento(CodificatoreMessagio,DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        super().__init__()
        self.chiave : int = chiave

    def sposta_caratteri(self, c: str):
        lettere : str = string.ascii_lowercase
        numeri = range(1, len(lettere) + 1)
        diz : dict[str, int] = dict(zip(lettere, numeri))
        if c in diz.keys():
            self.chiave += diz[c]
            n = self.chiave
            for k,v in diz.items():
                if n == v:
                    return k


    def codifica(self, testoInChiaro: str):
        for i in testoInChiaro:
            risultato : str = ""
            self.sposta_caratteri(i)
            risultato.join(i)
        return risultato

class CifratoreACombinazione(CodificatoreMessagio, DecodificatoreMessaggio):
    def __init__(self, n: int) -> None:
        super().__init__()
        self.n : int = n

    def codifica(self, testoInChiaro: str) -> str:
        i = 0
        combinazione : str = ""
        while i == self.n:
            a : int = int(len(testoInChiaro)/2)
            stringa1 = testoInChiaro[0 : a]
            stringa2 = testoInChiaro[a -1 : -1]
            for i in stringa1, stringa2:
                combinazione = zip()

            


