from abc import abstractmethod, ABC
class Pagamento(ABC):

    def __init__(self):
        pass

    def setPagamento(self, importo: float):
        self.__importo = round(importo, 2)
        return self.__importo
    
    def getPagamento(self):
        return self.__importo
    
    @abstractmethod
    def dettagliPagamento(self):
        pass
    

class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        print(f"Pagamento in contanti di: {self.getPagamento()}") 

    def inPezziDa(self):
        
        self.pezzi : dict[float, int] = {500.00 : 0, 200.00 : 0, 100.00 : 0, 50.00 : 0, 20.00 : 0, 10.00 : 0, 5.00 : 0, 2.00 : 0, 1.00 : 0,
                                         0.50 : 0, 0.20 : 0, 0.10 : 0, 0.05 : 0, 0.02 : 0, 0.01: 0}
        importo = self.getPagamento()
        print(f"Pagamento in contanti di {self.getPagamento()}\n"
                f"{self.getPagamento()} euro da pagare in:")
        while importo != 0:
            for k,v in self.pezzi.items():
                if round(importo,2) >= k:
                    importo = round(importo-k,2)
                    self.pezzi[k] = 1 + v
                    break

        for k,v in self.pezzi.items():
            if v > 0:
                if k >= 5:
                    print(f"{v} banconota da {k}")
                else:
                    print(f"{v} monete da {k}")

class PagamentoCarteCredito(Pagamento):
    
    def __init__(self, nome_titolare: str, data_di_scadenza: str, numero_carta: int ):
        super().__init__()
        self.nome_titolare : str = nome_titolare
        self.data_di_scadenza : str = data_di_scadenza
        self.numero_carta : int = numero_carta

    def dettagliPagamento(self):
        
        print(f"Pagamento di: €{self.getPagamento()}\n"
               f"Nome sulla carta: {self.nome_titolare}\n"
               f"Data di scadenza: {self.data_di_scadenza}\n"
               f"Numero di carta: {self.numero_carta}")
                
                



        
                

importo = PagamentoContanti() # type: ignore
importo.setPagamento(352.20)
importo.inPezziDa()   


    