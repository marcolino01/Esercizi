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
        self.list_animal : list[str] = []

    def __str__(self) -> str:
        return f"Animal: (name = {self.name},species = {self.species}, age = {self.age})"
        

    


class Fence:
    def __init__(self, area: float, 
                temperature: float, 
                habitat: str):
        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.list_animal : list[str] = []

    def __str__(self) -> str:
        return f"Fence(area= {self.area}, temperature={self.temperature}, habitat={self.habitat})"



class ZooKeepers:
    def __init__(self, name: str, 
                 surname: str, 
                 id: int, ):
        self.name : str = name
        self.surname : str = surname
        self.id : int = id
    
    def add_animal(self, animals: Animal, fence: Fence):
        if animals.preferred_habitat == fence.habitat:
            if animals.area_animal <= fence.area:
                fence.list_animal.append(animals)
                fence.area -= animals.area_animal
            else:
                print("The fence is full")
        else:
            print("Sorry the animal doesn't like this habitat")
            

    def remove_animal(self, animal: Animal, fence: list[Fence]):
        fence.list_animal.remove(animal)
        fence.area +=  animal.area_animal

    def feed(self, animal: Animal):
        if animal.health < 100:
            self.new_width : Animal = round(animal.width * (1 + 2/100),2)
            self.new_height : Animal = round(animal.height * (1 + 2/100),2)
            self.new_areaanimal = round(self.new_height * self.new_width)
            self.new_health = round(animal.health * (1 + 1/100),2)
            self.area_fence = fence.area
            if self.new_areaanimal <= self.area_fence:
                animal.health = self.new_health
                animal.width = self.new_width
                animal.height = self.new_height
                fence.area -= self.new_areaanimal
        return animal.health
        
    
    
    def clean(self,fence: Fence):
        self.area_animal = Animal(self.area_animal)
        self.area_residua = fence.area
        self.time : float = sum(self.area_animal) / self.area_residua
        
        if self.time == 0:
            self.time = self.area_animal

        return self.time
        

    def __str__(self) -> str:
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"


class Zoo:
    def __init__(self, zookeepers: list[ZooKeepers] =[], fence: list[Fence] = [], animals : list[Animal] = []):
        self.zookepers : list[ZooKeepers] = zookeepers
        self.fence : list[Fence] = fence
        self.animals : list[Animal] = animals

    def describe_zoo(self):
        print("Guardians:")
        for guardian in self.zookepers:
            print(guardian.__str__())
        
        print("\nFences:")
        for fence in self.fence:
            print(fence.__str__())

        print("\nAnimals:")
        for animal in self.animals:
            print(animal.__str__())

keeper = ZooKeepers(name="John", surname="Doe", id=1)
fence = Fence(area=1000, temperature=25, habitat="Savana")
lion = Animal(name="Leone", species="Panthera leo", age=5, height=2, width=3, preferred_habitat="Savana")
zoo = Zoo(zookeepers=[keeper], fence=[fence], animals=[])
keeper.add_animal(lion, fence)
zoo.describe_zoo()

        
    

