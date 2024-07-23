from abc import (ABC, abstractmethod)

class Volo(ABC):
    def __init__(self, codiceVolo: str, capacità: int, prenotazioni: int = 0) -> None:
        self.codiceVolo : str = codiceVolo
        self.capacità : int = capacità
        self.prenotazioni : int = prenotazioni

    @abstractmethod
    def prenota_posto(self, posti: int, classe_servizio: str)-> str:
        pass

    @abstractmethod
    def posti_disponibili(self)-> int:
        pass

class VoloCommerciale(Volo):
    def __init__(self, codiceVolo: str, capacità: int, prenotazioni: int = 0) -> None:
        super().__init__(codiceVolo, capacità, prenotazioni)
        self.posto_economica : int = round(0.7* self.capacità)
        self.posti_business : int = round(0.2* self.capacità)
        self.posti_prima : int = self.capacità - (self.posto_economica + self.posti_business)
        self.diz : dict[str,int] = {"posti disponibili" : self.capacità,
                                    "classe economica": self.posto_economica,
                                    "classe business" : self.posti_business,
                                    "classe prima" : self.posti_prima}
        
        self.prenotazione_economica : int = 0
        self.prenotazione_business : int = 0
        self.prenotazione_prima : int = 0
    
    def posti_disponibili(self)-> int:
        if self.capacità - self.prenotazioni:
            for k in self.diz.keys():
                if classe_
    
    def prenota_posto(self, posti: int, classe_servizio: str)-> str:
        if posti <= self.posti_disponibili():
            for k in self.diz.keys():
                if classe_servizio.lower() == k:
                    if posti <= self.diz[k]:
                        self.diz[k]-= posti
                        return f"Hai riservato {posti} posti in {self.diz[k]}"
                    else:
                        return f"Non è possibile riservare {posti} posti in {k}. Numero posti disponibili: {self.posti_disponibili()}"
                else:
                    return f"Siamo spiacenti la {classe_servizio} non esiste "
        else:
            return(f"Siamo spiacenti il volo {self.codiceVolo} è al completo")    

class VoloCharter(Volo):
    def __init__(self, codiceVolo: str, capacità: int, prenotazioni: int = 0) -> None:
        super().__init__(codiceVolo, capacità, prenotazioni)
        


        
