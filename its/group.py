class Group:

    def __init__(self, name: str, limits_students: int):
        self.name : str = name
        self.limits_students : int = limits_students

    def get_name(self):
        return self.name
    
    def get_limits(self):
        return self.limits_students