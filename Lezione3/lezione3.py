#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names 
#in a list, and then use a for loop to print the name of each pizza.• Modify your for loop 
#to print a sentence using the name of the pizza, instead of printing just the name of the
#pizza. For each pizza, you should have one line of output containing a simple statement 
#like I like pepperoni pizza.• Add a line at the end of your program, outside the for loop, 
#that states how much you like pizza. The output should consist of three or more lines about 
#the kinds of pizza you like and then an additional sentence, such as I really love pizza!
import copy


type_of_pizza : list[str] = ["margherita","boscaiola", "crostino"]

for i in type_of_pizza:
    print(f"mi piace davvero la pizza {i}")
print("mi piace un sacco la pizza")

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name
# of each animal.• Modify your program to print a statement about each animal, such as A 
#dog would make a great pet.• Add a line at the end of your program, stating what these
#animals have in common. You could print a sentence, such as Any of these animals would 
#make a great pet!

pets: list[str] = ["cane","gatto","tartaruga"]

for i in pets:
    print(f"{i} è un ottimo animale domestico")
print("sarebbero tutti degli ottimi animali domestici")


#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
#4-4. One Million: Make a list of the numbers from one to one million, and then use a
# for loop to print the numbers. (If the output is taking too long, stop it by pressing 
#CTRL-C or by closing the output window.)

for x in range (0,21):
    print(x)

lista_numeri: list[int] = list(range(1000001))
"""print(lista_numeri)"""
#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use 
#min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.

print(min(lista_numeri),max(lista_numeri))
print(sum(lista_numeri))


#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the 
#odd numbers from 1 to 20. Use a for loop to print each number.

dispari: list[int] = []
lista20: list[int] = list(range(0,21))
for x in lista20:
    if x%2 != 0:
        dispari.append(x)
print(dispari)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print 
#the numbers in your list.

multipli3: list[int] =[]
for x in range (3,31,3):
    multipli3.append(x)
print(multipli3)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube
#of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube
# of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubi: list[int] = []
for x in range(1,10):
    y = x**3
    cubi.append(y)
print(cubi)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes: list[int]= [x**3 for x in range(1,11)]
print(cubes)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to
#the end of the program that do the following:• Print the message The first three items 
#in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print
#three items from the middle of the list.• Print the message The last three items in 
#the list are:. Then use a slice to print the last three items in the list.


print(cubi[:3])
print(cubi[-3:])

mid = len(cubi) // 2
print(cubi[mid-1],cubi[mid],cubi[mid+1])



#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print 
#the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

friend_pizzas : list[str] = copy.deepcopy(type_of_pizza)
type_of_pizza.append("diavola")
friend_pizzas.append("bufala")

print(type_of_pizza)
print(friend_pizzas)
print(f"my favorite pizzas are {type_of_pizza}")
print(f"my favorite pizzas are {friend_pizzas}")


#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of
#foods.py, and write two for loops to print each list of foods.

for i in type_of_pizza:
    print(i)
for i in friend_pizzas:
    print(i)

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.
car : str = "Audi"
dog : str = "Labrador"
moto : str = "Yamaha"
city : str = "Rome"
nation : str = "Italy"
print("Is car==?Audi?? I predict True")
print(car=="Audi")
print("Is car=='Italy'? I predict False")
print(car=="Italy")
print("Is dog=='Labrador'? i predict True")
print(dog=="Labrador")
print("is dog=='Audi'? I predict False")
print(dog=='Audi')
print("is moto=='Yamaha'? I predict True")
print(moto=="Yamaha")
print("Is moto=='Rome'?I predict False")
print(moto=='Rome')
print("is city=='Rome'? I predict True")
print(city=="Rome")
print("Is city=='Italy? I predict False")
print(city=="Italy")
print("Is nation=='Italy? I predict True")
print(nation=="Italy")
print("Is nation=='Audi'? I predict False")
print(nation=="Audi")

#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. Have at least one True and one False result for each of the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list
str1 : str = "ciao"
str2 : str = "CIAO"
print("is str1==str2?I predict False")
print(str1==str2)
print("is str1==str2(lower)?I predict True")
print(str1==str2.lower())
a : int = 5
b : int = 6
print("is a==b?I predict False")
print(a==b)
print("is a<b? i predict True")
print(a<b)
print("is a>b? i predict False")
print(a>b)

if 4<5 and 4>3:
    print(True)
if 4<5 or 4<3:
    print(False)
lista : list = [1,2,3,4,5]
ab : str = int(input())
if ab in lista:
    print(True)
else:
    print(False)


#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.
#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color : str = input("scegli un colore tra verde giallo o rosso : ->")
if alien_color == "verde":
    print("hai guadagnato 5 punti ")
elif alien_color == "giallo":
    print("hai guadagnato 10 punti")
elif alien_color == "rosso":
    print("hai guadagnato 15 punti")
else:
    print("ti ho detto di inserire verde giallo o rosso")


#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.

age : str = int(input("inserisci età: ->"))

if age < 2:
    print("the person is a baby")
elif 2 <= age < 4:
    print("the person is a toddler")
elif 4 <= age < 13:
    print("the person is a kid")
elif 13 <= age < 20:
    print("the person is a teenager")
elif 20 <= age < 65:
    print("the person is an adult")
else:
    print("the person is an elder")

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
#independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is 
#in your list. If the fruit is in your list, the if block should print a statement, 
#such as You really like Apples!

frutta : str = input("inserisci un frutto: ")
favorite_fruit : list[str] = ["mele","pesche","fragole"]

if frutta in favorite_fruit and frutta == "mele":
    print("ti piaccione molto le mele")
elif frutta in favorite_fruit and frutta == "fragole":
    print("ti piacciono molto le fragole")
elif frutta in favorite_fruit and frutta == "pesche":
    print("ti piacciono molto le pesche")
else: 
    print("questo frutto non mi piace")


#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they 
#log in to a website. Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would 
#you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed.


usernames : list[str] = []

if len(usernames) == 0:
        print("We need to find some users!")
else:
    for i in usernames:
        if i == "Admin":
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"hello {i}, thank you for logging in again")



#5-10 Do the following to create a program that simulates how websites ensure that everyone 
#has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new 
#usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. 
#If it has, print a message that the person will need to enter a new username. If a 
#username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should 
#not be accepted. (To do this, you’ll need to make a copy of current_users containing 
#the lowercase versions of all existing users.)
current_users : list[str] = ["Marco","Davide","Francesca","Filippo"]
new_users : list[str] = ["Marco","Lorenzo","Gaia","Filippo"]
current_users : list[str] = [i.lower() for i in current_users]
new_users : list[str] = [i.lower() for i in new_users]
username_comuni : list[str] = []
username_ok : list[str] = []
for i in current_users:
    if i in new_users:
        username_comuni.append(i)
    else:
        username_ok.append(i)
print(f"l'username {username_comuni} esiste gia")
print(f"l'username {username_ok} è disponibile")

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st 
#or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for 
#each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and 
#each result should be on a separate line.
        
numbers : list[int] = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    if i == 1:
        print(f"{i} is the first")
    elif i == 2:
        print(f"{i} is the second")
    elif i == 3:
        print(f"{i} is the 3th")
    elif i == 4:
        print(f"{i} is the 4th")
    elif i == 5:
        print(f"{i} is the 5th")
    elif i == 6:
        print(f"{i} is the 6th")
    elif i == 7:
        print(f"{i} is the 7th")
    elif i == 8:
        print(f"{i} is the 8th")
    elif i == 9:
        print(f"{i} is the 9th")
        

    
    
            

     





