#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
#Make a separate file that imports Restaurant. Make a Restaurant instance, and call 
#one of Restaurant’s methods to show that the import statement is working properly.

from es_obbligatori import Restaurant

restaurant : Restaurant = Restaurant("gigi","cucina italiana",90)

restaurant.describe_restaurant()

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, 
#Privileges, and Admin in one module. Create a separate file, make an Admin instance, 
#and call show_privileges() to show that everything is working correctly.

from es_obbligatori import User, Admin, Privileges

user1 = Admin("Marco", "Di Cicco", 23, "Ladispoli")
user1.privileges.show_privileges()