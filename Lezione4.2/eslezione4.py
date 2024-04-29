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

while 

