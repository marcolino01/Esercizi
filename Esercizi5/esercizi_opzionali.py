"""1. Create a Playlist:
Write a function called create_playlist() that accepts a playlist name and a variable number 
of song titles. The function should return a dictionary with the playlist name and a set of 
songs. Call the function with different numbers of songs to demonstrate flexibility.
Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
Write a function called add_like() that accepts a dictionary, the name of a playlist, 
and a boolean value indicating whether it is liked (True or False). This function should 
return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)"""

def create_playlist(name : str, *songs : str)-> dict:
    playlist : dict = {
        'name' : name,
        'songs' : [songs]
    }
    return playlist

print(create_playlist("marco","kid yugi","franco"))


"""Write a function called add_book() that accepts an author's name and a variable number of 
book titles authored by them. This function should return a dictionary where the author's 
name is the key and the value is a list of their books. Demonstrate this function by adding 
books for different authors.
Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author 
from whom to remove all details. This function should return an updated dictionary.
Example: delete_book(dictionary, “Mark Twain”)"""

def add_book(author: str, *books: str)->dict:
    book : dict = {
        "name": author,
        "title": [books]
    }
    if author in books:
        book[author].extend(books)
    else:
        book[author] = list[books]
    return book

print(add_book("Stephen King", "IT","Carrie","Pet Sematary"))

def delete_book(author: str, *books: str)->dict:
    if books in author:
        del author[books]
    else:
        print("In this dictionary there isn't this book")
    return author

author_books = add_book("Charles Dickens", "Great Expectations", "A Tale of Two Cities", "Oliver Twist")
print(author_books)

author_books = delete_book(author_books, "Charles Dickens")
print(author_books)

    
"""3. Personal Info:
Write a build_profile() function that accepts the name , surname,  occupation, location, and 
age  of a person. Make occupation, location, and age optional parameters. Use this function 
to create profiles for different people, demonstrating how it handles these optional parameters.
Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)"""

def build_profile(name: str, surname: str, occupation = None, location = None, age = None)->dict:
    profile : dict = { "name": name,
                      "surname": surname}
    if occupation:
        profile["occupation"] = occupation
    if location:
        profile["location"] = location
    if age:
        profile["age"] = age
    return profile

print(build_profile("marco","di cicco",age=23))

"""4. Event Organizer:
Write a function called plan_event() that accepts an event name, a list of participants,
 and an hour. The function should return a dictionary that includes the event name and a 
 list of the participants. Call this function with varying numbers of participants to plan 
 different events.
Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)
Write a function called modify_event() that accepts a dictionary, an event name, and new 
details to modify an already planned event.
Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)"""

def plan_event(event_name : str, participants : list[str], hour: str)->dict:
    event : dict = {"event_name": event_name,
                    "participants": participants,
                    "hour": hour}
    return event

print(plan_event("festa",["marco","lorenzo"],"4pm"))

"""5. Shopping List:
Write a function called create_shopping_list() that accepts a store name and any number of 
items as arguments. It should return a dictionary with the store name and a set of items to 
buy there. Test the function with different stores and item lists.
Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
Write a function called print_shopping_list() that accepts a dictionary and a store name, 
then prints each item from that store's shopping list.
Example: print_shopping_list(dictionary, "Grocery Store")"""

def create_shopping_list(name : str, *items : str)->dict:
    shop_list : dict = {"name": name,
                        "item": items}
    return shop_list
print(create_shopping_list("LIDL","Milk","Bread","Eggs"))

    
