"""Exercise 4 (Folder 9 ex_4.py)
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu"""

class Food:
    def __init__(self, name : str, price : float, description : str = None):
        self.name: str = name
        self.price: float = price
        self.description: str = description

    def __str__(self)->str:
        if self.description:
            return f"menu {self.name} ,price= {self.price}, {self.description}"
        else:
            return f"menu {self.name}, price= {self.price}"

lasagna = Food("lasagna", 7.50, "pasta")
tiramisù = Food("tiramisù", 5, "dolce")
bistecca = Food("bistecca", 11.50, "carne")

class Menù:
    def __init__(self,foods : list[Food] = [])->list[str]:
        self.foods: list[Food] = foods

    def addFood(self,food: Food)->list[str]:
        count = 0 
        for food_menu in self.foods:
            if food.name == food_menu.name:
                count +=1 
                food.price = food_menu.price                                         #EMULAZIONE DI UN SEEEEEEET
        if count == 0:
            self.foods.append(food)

    def removeFood(self,food: Food)->list[str]:
        if food in self.foods:
            self.foods.remove(food)

    def getAvgPrice(self):
        total_sum: float = 0
        for food in self.foods:
            total_sum += food.price
            avg_price: float = total_sum/ len(self.foods)
        return avg_price
    
    def __str__(self) -> str:
        repr: str = ""
        for food in self.foods:
            repr += food.__str__()
        avg_price: float = self.getAvgPrice()
        repr += f'il prezzo medio è {avg_price}'
        return repr 

menu:Menù = Menù()
menu.addFood(tiramisù)
menu.addFood(lasagna)
print(menu)
menu.removeFood(tiramisù)
print(menu)
