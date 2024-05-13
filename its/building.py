from room import Room

class Building:


    def __init__(self, name : str, address: str, floors: tuple[int,int]):
        self.name : str = name
        self.address : str = address
        self.floors : int = floors
        self.rooms : list[Room] = []

    def set_name(self, name:str):
        self.name = name
    
    def get_name(self)-> str:
        return self.name
    
    def set_address(self, address:str):
        self.address = address

    def get_address(self)-> str:
        return self.address
    
    def set_floors(self, floors:str):
        self.floors = floors
    
    def get_floors(self)-> str:
        return self.floors
    

    def add_room(self,room: Room)-> bool:
        lower, upper = self.get_floors()
        if room not in self.get_rooms() and lower<= room.floor <= upper:
            self.rooms.append(room)
            return True
        return False
    
    def __str__(self) -> str:
        s : str = f"building(name= {self.get_name()}, address= {self.get_address()}, floors= {self.get_floors()})"
        s += "\nwith Romms:\n"
        for room in self.get_room():
            s +=. _



 