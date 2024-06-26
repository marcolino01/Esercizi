# Marco Di Cicco
# 18/04/2024




print("Hello World")

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d
# like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

#this list contain the name
name : list = ["Mamma","Papà","Andrea","Francesco"]

for i in name:
    message: str =f"{i} vorresti venire a cena?"
    print(message)




#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.


name[3] = "Nonna"

for i in name:
    message: str =f"{i} vorresti venire a cena?"
    print(message)


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

#add new guests
name.insert(0,"Zia")
name.insert(2,"Zio")
name.append("Jacopo")

for i in name:
    message: str =f"{i} vorresti venire a cena?"
    print(message)



#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


#remove guests
sorry : list = []

for idx, i in enumerate(name):
    if idx < 3:
        print(i)
    else:
        delate: str = name.pop(idx)
        sorry.append(delate)        
print(sorry)



#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

place : list[str] = ["New York","Malaga","Kenya","Giappone","Norvegia"]
print(place)
print(sorted(place))
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
#use len() to print a message indicating the number of people you’re inviting to dinner.


message2: str = f"il numero degli invitati a cena è {len(name)}"
print(f"{message2}")


#3-10. Every Function: Think of things you could store in a list. For example, you could make 
#a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write 
#a program that creates a list containing these items and then uses each function introduced 
#in this chapter at least once.

place : list[str] = ["New York","Malaga","Kenya","Giappone","Norvegia"]
place.insert(0,"Burundi")
place.insert(3,"Mozambico")
place.append("Parigi")
print(place)
place.pop(5)
print(place)
print(sorted(place))
print(sorted(place, reverse= True))
print(place)
place.sort()
print(place)
place.sort()
print(place)
place.reverse()
print(place)

#6-1. Person: Use a dictionary to store information about a person you know. Store their first
#name, last name, age, and the city in which they live. You should have keys such as 
#first_name, last_name, age, and city. Print each piece of information stored in your 
#dictionary.

anagrafica: dict = [{"nome": "Marco",
                    "cognome": "Di Cicco",
                    "age": "23",
                    "city": "Ladispoli"},
{                   "nome": "Lorenzo",
                    "cognome": "Peluso",
                    "age": "22",
                    "city": "Ladispoli"},
{                   "nome": "Leonardo",
                    "cognome": "Servetti",
                    "age": "23",
                    "city": "Ladispoli"},
{                   "nome": "Stefano",
                    "cognome": "Regano",
                    "age": "22",
                    "city": "Monaco"},
{                   "nome": "Gaia",
                    "cognome": "Flati",
                    "age": "23",
                    "city": "Ladispoli"}
]
print(anagrafica)
print(anagrafica[0].keys())
print(anagrafica[1].values())

for i in anagrafica:
    print(i["nome"])
 
for i in anagrafica:
    print(i["cognome"])

for i in anagrafica:
    print(i["age"])

for i in anagrafica:
    print(i["city"])

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five 
#names, and use them as keys in your dictionary. Think of a favorite number for each person, 
#and store each as a value in your dictionary. Print each person’s name and their favorite 
#number. For even more fun, poll a few friends and get some actual data for your program.
anagrafica[0]["numero preferito"]= 9
anagrafica[1]["numero preferito"]= 22 
anagrafica[2]["numero preferito"]= 10
anagrafica[3]["numero preferito"]= 16
anagrafica[4]["numero preferito"]= 23


for i in anagrafica:
    print(f"{i['nome']} e il numero suo preferito è {i['numero preferito']}")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.• Think of five programming words 
#you’ve learned about in the previous chapters. Use these words as the keys in your glossary, 
#and store their meanings as values.• Print each word and its meaning as neatly formatted 
#output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning
#pair in your output.

glossary: dict =[{"append()": "adds an element to the end of the list "},
                 {"insert()": "inserts an element at a specified position"},
                 {"pop()": "removes the element at a given position and returns it"},
                 {"sort()": "sorts the list elements on the spot"},
                 {"reverse()": "reverses the order of the list elements"}]

for i in glossary:
    for keys,values in i.items():
        print(f"{keys}: {values}")


#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries 
#representing different people, and store all three dictionaries in a list called people.
#Loop through your list of people. As you loop through the list, print everything you 
#know about each person.

anagrafica2 : dict = {"nome": "Federica",
                      "cognome" : "Buccella",
                      "age": "23",
                      "city": "Ladispoli",
                      "numero preferito": "5"}
anagrafica3 : dict = {"nome": "Tiziano",
                      "cognome": "Montesano",
                      "age": "22",
                      "city": "Ladispoli",
                      "numero preferito": "8"}

anagrafica.append(anagrafica2)
print(anagrafica)
anagrafica.append(anagrafica3)
print(anagrafica)

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. Store these 
#dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 

animals : dict = [{"animal": "cane",
                  "owner": "Marco"},
                  {"animal": "gatto",
                   "owner": "Lorenzo"}]
animals2 : dict = {"animal" : "tartaruga", 
                   "owner": "Davide"}

pets : dict = {}
animals.append(animals2)
print(animals)
pets=animals
print(pets)


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names 
#to use as keys in the dictionary, and store one to three favorite places for each person.
# To make this exercise a bit more interesting, ask some friends to name a few of their 
#favorite places. Loop through the dictionary, and print each person’s name and their 
#favorite places.


favourite_places : dict = [{"name" : "Marco",
                            "places": "Roma,Parigi,Napoli"},
                            {"name" : "Lorenzo",
                             "places" : "Napoli, New York"}]
for i in favourite_places:
    print(f"i posti preferiti di {i['name']} sono {i['places']}")



#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have
#more than one favorite number. Then print each person’s name along 
#with their favorite numbers.

anagrafica[0]["numero preferito"] = 9, 10
anagrafica[3]["numero preferito"] = 10, 13

for i in anagrafica:
    print(f"i numeri preferiti di {i['nome']} sono {i['numero preferito']}")



#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys 
#in your dictionary. Create a dictionary of information about each city and include the 
#country that the city is in, its approximate population, and one fact about that city. 
#The keys for each city’s dictionary should be something like country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.

cities : dict = [{"city": "New York",
                  "country": "USA",
                  "population": "8 mln",
                  "monument": "Statue of Liberty"},
                  {"city": "Roma",
                   "country": "Italy",
                   "population": "2,8 mln",
                   "monument": "Colosseo"},
                   {"city": "Paris",
                    "country": "France",
                    "popolution": "2,1 mln",
                    "monument": "Eiffel's Tower"}]

for i in cities:
    print(f"questi sono i dati di {i['city']} : {i}")