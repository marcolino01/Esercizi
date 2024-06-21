from abc import abstractmethod, ABC

class Forma(ABC):
    
    def __init__(self, nome: str):
        self.nome : str = nome 

    @abstractmethod
    def getArea(self)-> float:
        pass

    def render(self):
        pass

class Quadrato(Forma):

    def __init__(self,lato : float, nome: str = 'Quadrato'):
        super().__init__(nome)
        self.lato : float = lato

    def getArea(self):
        area = self.lato ** 2
        return area
    
    def render(self):
        
    



         


    
