class Animal:
    def __init__(self, name: str,
                species: str, 
                age: int, 
                height: float, 
                width: float, 
                preferred_habitat: str,):
        self.name : str = name
        self.species : str = species
        self.age : str = age
        self.height : float = height
        self.width : float = width
        self.preferred_habitat : str = preferred_habitat
        self.health : float = round(100 * (1 / age), 3)
        self.area_animal : float = height * width 
        

    


class Fence:
    def __init__(self, area: float, 
                temperature: float, 
                habitat: str):
        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat



class ZooKeepers:
    def __init__(self, name: str, 
                 surname: str, 
                 id: int, ):
        self.name : str = name
        self.surname : str = surname
        self.id : int = id
    
    def add_animal(self, animals: Animal, fence: list[Fence]):
        if Animal.preferred_habitat == Fence.habitat:
            if Animal.area_animal <= Fence.area:
                animals.append(fence)
                Fence.area = Fence.area - Animal.area_animal
            

    def remove_animal(self, animal: Animal, fence: list[Fence]):
        fence.remove(animal)
        Fence.area = Fence.area + Animal.area_animal

    def feed(self, animal: Animal):
        self.new_width : Animal = Animal.width * (1 + 2/100)
        self.new_height : Animal = Animal.height * (1 + 2/100)
        self.new_areaanimal = self.new_height * self.new_width
        self.new_health = Animal.health * (1 + 1/100)

        if self.new_areaanimal <= Fence.area:
            Animal.health = self.new_health
        
        return Animal.health
        
    
    
    def clean(self,fence: Fence):
        self.area_residua = Fence.area - Animal.area_animal
        self.time : float = Animal.area_animal / self.area_residua
        
        if self.time == 0:
            self.time = Animal.area_animal

        return self.time
        






class Zoo:
    def __init__(self, zookeepers: list[ZooKeepers] =[], fence: list[Fence] = [], animals : list[Animal] = []):
        self.zookepers : list[ZooKeepers] = zookeepers
        self.fence : list[Fence] = fence
        self.animals : list[Animal] = animals
