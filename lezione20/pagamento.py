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

        while importo != 0:
            for k,v in self.pezzi.items():
                if round(importo,2) > k:
                    importo -= k
                    self.pezzi[k] = 1 + v
        for v in self.pezzi.values():
            if v > 0:



        
                

importo = PagamentoContanti() # type: ignore
importo.setPagamento(352.20)
importo.inPezziDa()   


    