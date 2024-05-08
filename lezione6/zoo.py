class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health : float):
        self.name : str = name
        self.species : str = species
        self.age : str = age
        self.height : float = height
        self.width : float = width
        self.preferred_habitat : str = preferred_habitat
        self.health : float = health
        health : float = 100*(1/age)
        

    


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat



class ZooKeepers:
    def __init__(self, name: str, surname: str, id: int, ):
        self.name : str = name
        self.surname : str = surname
        self.id : int = id
    
    def add_animal(self, animals: Animal, fence: Fence):
        if self.preferred_
        
        
        
        
    def remove_animal(self,animal: Animal):



class Zoo:
    def __init__(self, zookeepers: list[ZooKeepers] =[], fence: list[Fence] = [], animals : list[Animal] = []):
        self.zookepers : list[ZooKeepers] = zookeepers
        self.fence : list[Fence] = fence
        self.animals : list[Animal] = animals
