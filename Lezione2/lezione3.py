#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names 
#in a list, and then use a for loop to print the name of each pizza.• Modify your for loop 
#to print a sentence using the name of the pizza, instead of printing just the name of the
#pizza. For each pizza, you should have one line of output containing a simple statement 
#like I like pepperoni pizza.• Add a line at the end of your program, outside the for loop, 
#that states how much you like pizza. The output should consist of three or more lines about 
#the kinds of pizza you like and then an additional sentence, such as I really love pizza!
type_of_pizza : list[str] = ["margherita","boscaiola", "crostino"]

for i in type_of_pizza:
    print(f"mi piace davvero la pizza {i}")
print("mi piacce un sacco la pizza")

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name
# of each animal.• Modify your program to print a statement about each animal, such as A 
#dog would make a great pet.• Add a line at the end of your program, stating what these
#animals have in common. You could print a sentence, such as Any of these animals would 
#make a great pet!

pets : list[str] = ["cane","gatto","tartaruga"]

for i in pets:
    print(f"{i} è un ottimo animale domestico")
print("sarebbero tutti degli ottimi animali domestici")


#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
#4-4. One Million: Make a list of the numbers from one to one million, and then use a
# for loop to print the numbers. (If the output is taking too long, stop it by pressing 
#CTRL-C or by closing the output window.)

i= 0 
for x in range (0,21):
    print(x)
    i+=1
lista_numeri: list[int] = list(range(1000001))
"""print(lista_numeri)"""
#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use 
#min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.

print(min(lista_numeri),max(lista_numeri))
print(sum(lista_numeri))


#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the 
#odd numbers from 1 to 20. Use a for loop to print each number.

dispari : list[int] = []
lista20 : list[int] = list(range(0,21))
for x in lista20:
    if x%2!=0:
        dispari.append(x)
print(dispari)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print 
#the numbers in your list.

multipli3 : list[int] =[]
for x in range (3,31,3):
    multipli3.append(x)
print(multipli3)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube
#of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube
# of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubi : list[int] = []
for x in range(1,10):
    y=x**3
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

mid=len(cubi)//2
print(cubi[mid-1],cubi[mid],cubi[mid+1])


