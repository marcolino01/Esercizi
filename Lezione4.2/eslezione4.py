#8-1. Message: Write a function called display_message() that prints one sentence 
#telling everyone what you are learning about in this chapter. Call the function, 
#and make sure the message displays correctly.



def display_message(stringa: str ):
    return stringa
c : str = "sto imparando ad usare python"
print(display_message(c))

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function 
#should print a message, such as "One of my favorite books is Alice in Wonderland". 
#Call the function, making sure to include a book title as an argument in the
# function call.

def favorite_book(title : str)->str:
    print(f"one of my favorite book is {title}")
book : str = "Il piccolo principe"
favorite_book(book)

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt. The function should print a sentence 
#summarizing the size of the shirt and the message printed on it. Call the function 
#once using positional arguments to make a shirt. Call the function a second time 
#using keyword arguments.

def make_shirt(size : str, text : str)->str:
    print(f"la taglia della maglia è {size} e la stampa è {text}")
make_shirt("M","stampa maglia")
taglia : str = "L"
message : str = "testo"
make_shirt(taglia, message)


#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default 
#with a message that reads I love Python. Make a large shirt and a medium shirt with the 
#default message, and a shirt of any size with a different message.

def make_shirt(size : str, text : str, taglia : str = "L", message : str ="i love python")->str:
    print(f"la taglia della maglia è {size} e la stampa è {text}")
    print(f"la taglia della maglia è {taglia} e la stampa è {message}")
    print(f"la taglia della maglia è {size} e la stampa è {message}")
make_shirt("M","python")

#8-5. Cities: Write a function called describe_city() that accepts the name of a city 
#and its country. The function should print a simple sentence, such as Reykjavik is in 
#Iceland. Give the parameter for the country a default value. Call your function for 
#three different cities, at least one of which is not in the default country.

def describe_city(city : str, country : str = "Italy")->str:
    print(f"{city} is in Italy")
describe_city("Rome")
describe_city("Milano")
describe_city("Parigi")

#8-6. City Names: Write a function called city_country() that takes in the name of a city 
#and its country. The function should return a string formatted like this: "Santiago, Chile". 
#Call your function with at least three city-country pairs, and print the values that 
#are returned.

def city_country(city : str, country : str)->str:
    print(f"{city},{country}")
city_country("Paris","France")
city_country("New York","USA")
city_country("Rome","Italy")


#8-7. Album: Write a function called make_album() that builds a dictionary describing a music 
#album. The function should take in an artist name and an album title, and it should return a 
#dictionary containing these two pieces of information. Use the function to make three 
#dictionaries representing different albums. Print each return value to show that the  
#dictionaries are storing the album information correctly. Use None to add an optional 
#parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s 
#dictionary. Make at least one new function call that includes the number of 
#songs on an album.

def make_album(artist: str, title: str, songs :None)->dict:
    album  = {artist: {title: songs}}
    return album
print(make_album("Gazzelle", "Dentro", 10))
print(make_album("Gazzelle","Ok", None))
print(make_album("Gazzelle","Punk", None))

#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that 
#allows users to enter an album’s artist and title. Once you have that information, call 
#make_album() with the user’s input and print the dictionary that’s created. Be sure to 
#include a quit value in the while loop.
def make_album(artist: str, title: str, songs :None)->dict:
    album  = {artist: {title: songs}}
    return album

while True:
     artist = input("inserisci l'artista o 'x' per uscire:")
     if artist == 'x':
        break
     title = input("inserisci il titolo dell'album o 'x' per uscire:")
     if title == 'x':
        break
     print(make_album(artist,title,None))

 
 
#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a 
#function called show_messages(), which prints each text message.

list1 : list = ["ciao","marco","messaggio"]
def show_messages(lista: list)->list:
    for i in lista:
        print(i)
show_messages(list1)

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a 
#function called send_messages() that prints each text message and moves each message 
#to a new list called sent_messages as it’s printed. After calling the function, print 
#both of your lists to make sure the messages were moved correctly.

list1 : list = ["ciao","marco","messaggio"]
def show_messages(lista: list)->list:
    sent_messages : list = []
    for i in lista:
        print(i)
        sent_messages.append(i)
    print(list1,sent_messages)

show_messages(list1)


#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call 
#provides, and it should print a summary of the sandwich that’s being ordered. Call the 
#function three times, using a different number of arguments each time.


def items_sandwiches(list : str):
    print("nel sandwiches abbiamo")
    for i in list:
        print(i)
items_sandwiches(["cipolla","insalata","pomodoro"])
items_sandwiches(["bacon","cheese","bbq"])
items_sandwiches(["mayo","ketchup","cetriolo"])


#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first 
#and last names and three other key-value pairs that describe you. All the values must be 
#passed to the function as parameters. The function then must return a string such 
#as "Eric Crow, age 45, hair brown, weight 67"

build_profile : dict =  {"FirstName" : "Marco","LastName" : "Di Cicco","Age" : "23","HairColor" : "Brown","Weight" : "69"}

def profile(diz : dict)->str:
    for key in diz:
        print(f"{key},{diz.get()}")
profile(build_profile)

        
profile(build_profile)


