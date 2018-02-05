my_pizzas=['Chicken Tikka', 'Chicken Fajita','Afghnai']
friends_pizzas=my_pizzas[:]
print("My pizzas: \n"),
print(my_pizzas)
print("Friends pizzas: ")
print(friends_pizzas)

my_pizzas.append('Normal')                #use append method to add new element in my_pizzas list
friends_pizzas.append('20 inch')          #use append method to add new element in my_pizzas list

print("\nMy favorite pizzas are: ")
for mpizzas in my_pizzas:
    print(mpizzas)                         #new list with appended elemeny 'Normal'

print("\nMy friend's pizzas are: ")
for fp in friends_pizzas:
    print(fp)                               #new list with appended elemeny '20 inch'