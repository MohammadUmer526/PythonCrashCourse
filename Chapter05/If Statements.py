cars=['audi','bmw','toyota']

'''
#checking equality
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

bike='honda'
bike=='honda'
print(bike)

'''

''''
#checking inequality
request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print("Hold the anchovies")
else:
    print("Do not Hold")

'''

'''
#check multiple conditions

age_0=22
age_1=18
if age_0 >= 21 or age_1 >21:    #only first condition satisfy but not second condition but we have "or" that's why its consider only one condition to satisfy and printing true
    print("True")
else:
    print("False")

if age_0 >=21 and age_1 >19:     #satisfy both condition that's why it is givivg "true"
    print("True")
else:
    print("False")
'''

'''
#check whether value is in the list or not?
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' and 'onions'  in requested_topping:
    print("We found your itens!")
else:
    print("Item not found")
'''
'''
age = 50
if age < 18:
    print("You are not allowed")
elif age < 30:
    print("You are not allowed")
elif age > 40:
    print("You are allowed")
else:
    print("YOU ARE ALLOWED")
'''
'''
age=int(input("Enter your age: "))   #int() is use for type casting(converting string into integer)
if age <= 4:
    print("\nYour admission cost is $0")
elif age < 18:
    print("\nYour admission cost is: $5")
else:
    print("\nYour admission cost is: $10")
'''

'''
age=int(input("Enter your age: "))
if age <=4:
    price=0
    print("Your admission fee is: "+str(price))
elif age < 18:
    price=5
    print("\nYour admission cost is: "+str(price))
else:
    price=10
    print("\nYour admission cost is: "+str(price))
'''
'''
requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrroms")
if 'pepperoni' in requested_topping:
    print('Adding pepperoni')
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")
    print("Finished making pizza")
'''

'''
requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
elif 'pepperoni' in requested_topping:
    print("Adding pepperoni")
elif 'extra cheese' in  requested_topping:
    print("Adding extra cheese")
print("Finished making pizza")
'''

'''
requestes_topping=input("Enter topping: ")
if requestes_topping=="Mushrooms":
    print("Requested topping is: "+requestes_topping)
elif requestes_topping=="Extra cheese":
    print("Requested topping is: "+requestes_topping)
else:
    print("Requested topping not entered!")
'''

