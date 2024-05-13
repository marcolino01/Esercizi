from building import Building
from group import Group
class Course:

    def __init__(self, name: str, building : Building):
        self.name = name
        self.building = building
        self.groups : list[Group] = []

    



