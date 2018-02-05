'''
#Writing clear prompts

name = input("Enter your name: ")      #"input()" that ask user for input and pause the program until input is not recieved
message = "Hi, " + name + "!"
print(message)

'''

'''
prompt = "If you tell us who you are, we can personalize the messages you see.\n What is your name?"

name = input(prompt)
'''

#Using int() to accept Numerical Input
'''
age = input("How old are you?")
print(age)
'''

'''
age = input("How old are you?")

age = int(age)                      #use typecasting for converting
age >= 18
print(age)
'''

'''
#Roller Coaster

height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print("You are tall enough to ride!")
else:
    print("You are not allowed to ride")

'''

'''
#The Module Operator
number = input("Enter a number to find whether it is even or odd? ")
number = int(number)

if number % 2 == 0:
    print("The number " + str(number) + " is even")
else:
    print("the number " + str(number) + " is odd")
'''

'''
#The While Loop In Action
current_number  = 1                     #setting value
while current_number <=5:               #while loop for limitation of execution(5 0r less)
    print(current_number)
    current_number += 1                 #increement of 1

'''

'''
#Letting the The User Choose when to Quit
prompt = "\nTell me something, and I will repeat it back to you:"   #prompt for printing
prompt += "\nEnter 'quit' to end the program.:  "                   #prompt+ indicates contination of previous command
'''
'''
message = ""                                                        #printing message
while message!= 'quit':                                             #while loop
    message = input(prompt)                                         #passing input in var(messahe)
    print(message)
'''

'''
message = ""
while message !='quit':
    message = input(prompt)
    if message!='quit':
 
       print(message)
'''



'''

#Flag

prompt = "\nTell me something, and I will repeat it back to you:"   #prompt for printing
prompt += "\nEnter 'quit' to end the program.:  "                   #prompt+ indicates contination of previous command

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
'''

'''
#Using A Break To Exit Loop

msg = "Please enter a city where you want to vist: \nEnter quit when you are finished.\n"

while True:
    city = input(msg)

    if city != 'quit':
        print("You want to vist " + city.title() + "!\n")
    else:
        break
'''

'''

#Using Continue in A Loop
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)
'''


#Using While Loop With List And Dictionary
#Moving Items from One List to Another
'''
unconfirmed_users = ['john' , 'alice' , 'jen' , 'sarah']
comfirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    comfirmed_users.append(current_users)

    print("Verifiying users: "+current_users.title())

for comfirmed_user in comfirmed_users:
    print("\nVerifed user: "+comfirmed_user)
'''


'''
#Removing all instance of specific value from list

animal =['lion' ,'cat' , 'dog' ,'horse']

while 'horsse' in animal:
    animal.remove('horse')
print(animal)
'''

'''
#Filling A Dictionary With User Input

responses = {}                                                                      #create an empty dict

polling_active = True                                                               #generate flag
while polling_active:                                                               #condition

    name = input("What is your name: ")
    response = input("which mountain would you like to climb someday? ")

    responses[name] = response                                                     #store the reponse in name

    repeat = input("Would you like to let another person respond(yes/no) ")
    if repeat == 'no':                                                             #asking for more inputs
        polling_active = False                                                     #pop up false when enter 'no'

    print("\n---Polling Results---")

    for name , response in responses.items():
        print(name+ " would like to climb "+response +".")
'''