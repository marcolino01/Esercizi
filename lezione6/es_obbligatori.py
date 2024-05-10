"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant 
should store two attributes: a restaurant_name and a cuisine_type. Make a method called 
describe_restaurant() that prints these two pieces of information, and a method called 
open_restaurant() that prints a message indicating that the restaurant is open. Make an 
instance called restaurant from your class. Print the two attributes individually, and 
then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different 
instances from the class, and call describe_restaurant() for each instance.
9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called 
number_served with a default value of 0. Create an instance called restaurant from this 
class. Print the number of customers the restaurant has served, and then change this value 
and print it again. Add a method called set_number_served() that lets you set the number of 
customers that have been served. Call this method with a new number and print the value 
again. Add a method called increment_number_served() that lets you increment the number 
of customers who’ve been served. Call this method with any number you like that could 
represent how many customers were served in, say, a day of business."""

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number : int):
        self.restaurant_name : str = restaurant_name
        self.cuisine_type : str = cuisine_type
        self.number : int = number

    def describe_restaurant(self) -> str:
        print(f"Il ristorante {self.restaurant_name} serve {self.cuisine_type}")
        
    def open_restaurant(self)-> str:
        print(f"Il ristorante {self.restaurant_name} è aperto")

    def number_served(self, served: int)->int:
        self.number = served
        print(f"serviti : {self.number}")
        

    def increment_number_served(self, increment: int)->int:
        self.number += increment
        print(f"serviti a fine serata {self.number}")
    
ristorante = Restaurant("Da Gigi","Cucina romana", 70)
ristorante1 = Restaurant("ristorante messicano", "cucina messicana",13)
ristorante2 = Restaurant("ristorante giapponese", "cucina giapponese",40)
ristorante3 = Restaurant("ristorante thailandese","cucina thailandese",32)

"""print("nome del ristorante",ristorante.restaurant_name)
print("tipo di cucina", ristorante.cuisine_type)"""
ristorante.describe_restaurant()
ristorante.open_restaurant()
ristorante1.describe_restaurant()
ristorante2.describe_restaurant()
ristorante3.describe_restaurant()
ristorante1.open_restaurant()
ristorante2.open_restaurant()
ristorante3.open_restaurant()

ristorante.number_served(20)

ristorante.increment_number_served(5)



"""9-3. Users: Make a class called User. Create two attributes called first_name and 
last_name, and then create several other attributes that are typically stored in a user 
profile. Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.
9-5. Login Attempts: Add an attribute called login_attempts to your User class from 
Exercise 9-3. Write a method called increment_login_attempts() that increments the value 
of login_attempts by 1. Write another method called reset_login_attempts() that resets 
the value of login_attempts to 0. Make an instance of the User class and call 
increment_login_attempts() several times. Print the value of login_attempts to make sure 
it was incremented properly, and then call reset_login_attempts(). Print login_attempts again
 to make sure it was reset to 0."""

class User:
    
    def __init__(self, first_name: str,
                 last_name: str,
                 age:str, 
                 city: str, 
                 ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age : int = age
        self.city: str = city
        self.login_attempts: int = 0
    
    def describe_user(self) -> str:
        print(f"nome: {self.first_name}, cognome: {self.last_name}, età: {self.age}, città {self.city}")

    def greeting_user(self) -> str:
        print(f"È fantastico rivederti {self.first_name,self.last_name}")

    def increment_login_attempts(self) ->int:
            self.login_attempts += 1
            return self.login_attempts
    
    def reset_login_attempts(self) -> int:
        if self.login_attempts != 0:
            self.login_attempts = 0
        return self.login_attempts

user1 = User("Marco","Di Cicco",23,"Ladispoli")
user2 = User("Gianni","Rossi",56,"Poggibonzi")
user3 = User("Nina","Nino",29,"Mykonos")

user1.describe_user()
user1.greeting_user()
user2.describe_user()
user2.greeting_user()
user3.describe_user()
user3.greeting_user()

print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.reset_login_attempts())

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class 
called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or 
Exercise 9-4. Either version of the class will work; just pick the one you like better. Add 
an attribute called flavors that stores a list of ice cream flavors. Write a method that 
displays these flavors. Create an instance of IceCreamStand, and call this method. """

class IceCreamStand:
    def __init__(self, name : Restaurant, cuisine_type : Restaurant):
        self.flavors : list[str] = []
        self.name : Restaurant = name
        self.cuisine_type : Restaurant = cuisine_type

    def icecream_flavors(self,flavor : str) -> list[str]:
        self.flavors.append(flavor)

    def display_flavors(self)->str:
        for flavor in self.flavors:
            print(flavor)
    
gelateria  = IceCreamStand("Gelateria","artigianale")

gelateria.icecream_flavors("Fragola")
gelateria
