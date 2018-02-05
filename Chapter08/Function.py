'''
#Defining a Function
def grreting_user():                        #function defination
    """SDisplay a Simple Message"""         #docstring which defines what func does
    print("Welcome World")
grreting_user()                             #call the func
'''

'''
#Passing Information Through a Function
def greeting_member(username):
    print("Welcome "+username+ " to function in Python")
greeting_member("Muhammad")
'''

'''
#Getting Information in a Function
def greeting_input(msg):                                                #define func
    msg = input("What is your name: ")                                  #prompt user for input
    print("Wlecome "+msg.title()+ ", to input in function in Python")   #print message
greeting_input("")                                                      #passing null to fulfill arguement
'''

#Passing Arguments
#Positional Arguments
'''

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','herry')
'''

'''
#Multiple Arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'herry')
describe_pet('cat','tinker')
'''

'''
#Keyword Argument
#name value pair

def name_cities(country, continent):
    print("\nHe is from "+country.title()+ " which comes in "+continent.title())
name_cities(country='Pakistan',continent='Asia')
name_cities(country='U.K',continent='Europe')
name_cities(country='Turkey',continent='Europe and Asia')

'''

'''
#Returning A Simple Value
def get_formatted_named(first_name, last_name):
    """Retur  a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()
message= get_formatted_named('jimi', 'john')
print(message)
'''

'''
#Making An Argument Optional
def get_formatted_full_name(first_name, middle_name, last_name):        #create a func and pass parametter
    full_name = first_name + " " + middle_name + " " + last_name        #store parameter in a var(full_name)
    return full_name.title()                                            #return full_name in title case
message = get_formatted_full_name('Muhammad', 'Ali', 'Jinnah')          #outside the func to call it and passing argument in func, stores func in a var(message)
print(message)                                                          #print var(message) which contains function above
'''

'''
#Returning A Dictionary
def return_dict(first_name , last_name):                    #create func and passes parameters
    person = { 'first' : first_name ,'last' :  last_name}   #create a dict and declare values = parameter1(first_name) and parameter2(last_name)
    return  person                                          #return dict(person)
#print(return_dict('Muhammad','Umer'))                      #direct print funct() by passing arguments
message = return_dict('Muhammad', 'Ali' )                   #stroe func in a var(message) and passes arguments in funce
print(message)                                              #print var(message) above
'''

'''
def return_dict(f_name ,l_name, age=''):
    person = {'first' : f_name , 'last' : l_name }
    if age:
        person['age'] = age
    return person
print(return_dict('Muhammad', 'Ali',22))
'''

#Using A Function With While Loop
'''
def get_full_name(f_name, m_name, l_name):
    full_name = f_name + " " + m_name + " " + l_name
    return full_name

while True:
    print("\nPlease tell me your name!")
    f_name = input("Enter first name: ")
    m_name = input("Enter middle name: ")
    l_name= input("Enter your last name: ")

    formatted_name = get_full_name(f_name,m_name,l_name )
    print(formatted_name)
'''


'''
#For break in any timeWindows.old
def bio_info(f_name,l_name,age,city):
    bio = f_name + " " + l_name + " " + age + " " + city
    return bio

while True:
    print("\nPlease provide your information")
    first_name = input("Enter your first name: ")
    if first_name == 'q':
        break
    last_name = input("Enter your last name: ")
    if last_name == 'q':
        break
    age = input("Enter your age: ")
    if age == 'q':
        break
    city = input("Enter your city: ")
    if city == 'q':
        break
    print(bio_info(first_name,last_name,age,city))
'''

'''
#Passing A List

def greet_users(names):                             #declare a func and pass parameter in it(names)

    for name in names:                              #for loop for multiple elements in the list
        msg = "Welcome " + name.title() + "!"         #var(msg) which contains names(parametern)
        print(msg)
user_names = ['hannah' , 'ty' , 'margot']           #create a list
greet_users(user_names)                             #pass the argument
'''

'''
#Done with myself
def new_list(elements):

    for element in elements:
        msg = "Welcome " + element + "!"
        print(msg)

elements_arg = ['Hannah' , 'ty' , 'margot']
new_list(elements_arg)
'''

'''
def func(parameter):

    for parameters in parameter:
        msg = "Welcome " + parameters.title() + "!"
        print(msg)

arguments = ['warner' , 'smith' , 'stan']
func(arguments)
'''

'''
# Modifying List in a Function

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

completd_designs = []

while unprinted_designs:
    current_desgin = unprinted_designs.pop()

    completd_designs.append(current_desgin)

print("Completed Designs:")
for completd_design in completd_designs:
         print(completd_design.title())
'''

'''
#a = input("Enter a number")

add = False

print("Enter no for exit")
while True:
    a  = input("Enter a number: ")


    if a == 'no':
        break

    else:
        msg = "Your number after increement is: " + str(int(a) + 2)
        print(msg)


'''
'''
myfriend= ['umer' , 'saad' , 'ali']

while True:
    a = input("Do you want to add a friend or find a friend, enter f to find and a to add?")
    if a =='a':
        ab = input("Enter a name of a friend: ")
        myfriend.append(ab)
    elif a == 'f':
        for a in myfriend:'''


'''def users(user_names):

    for ib in user_names:
        msg= "Welcome " + ib.title() + "!"
        print(msg)
list_name=['Haya' , 'faizan','hassam']
users(list_name)


def greeting(names):                                    #funct in which passing a parameter(names) 
    for name in names:                                  #parameter names use in loop for iteration
        msg= "Welcome " + name.title() + "!"
        print(msg)
list_name = ['ali' , 'haya' ,'saad']                    #create a list
greeting(list_name)                                     #pass the argument in a which above list

'''

'''
#
unprinted_designs=['iphone case','robot padent' ,'dodecahedron']
complete_models=[]

while unprinted_designs:
    curent_designs=unprinted_designs.pop()
    print("Models:" +curent_designs)
x
    complete_models.append(curent_designs)

for complete_model in complete_models:
    print(complete_model)
'''

'''
def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing models: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone' , 'robot' , 'dodecahedron']
completed_models=[]
print_model(unprinted_designs,completed_models)
show_completed_models(completed_models)
'''

'''
def printed_model(unprinted_Designs,completed_models):          #define func with two parameter(list and secound list)
    while unprinted_Designs:                                    #loop for execute every element of list
        current_designs = unprinted_Designs.pop()               #poping element from main list and store in "current designs" loop

        print("Printing model: " +current_designs.title())      #printing each element which is copying
        completed_models.append(current_designs)                #appending elements in new list(completed)_models)

def show_completed_model(completed_models):                     #new function for new list with parameter for new list(completed_models)

    print("The followin models have been printed:")             #printing the new list statement
    for completed_model in completed_models:                    #for loop for inserting new list in var(complete_model) from complete_models
        print(completed_model.title())

list= ['iphone' , 'samsung' ,'zong']                            #outside the func create a list which will be copy in first func
completed_model=[]                                              #create a new list where list will be pasted
printed_model(list,completed_model)                             #passes the arguments for func_1 (list 1 and new empty list which is declared in above steps)
show_completed_model(completed_model)                           #passes the argument for func_2 because new list is accessing in func_2
'''


#Passing an Arbitary Number of Arguments
'''
def make_pizza(*toppings):                                      #make a func an pass parameter called(*topping) where *denotes to create an empty tuple which takes one or more elements and store in list
    print(toppings)                                             #print the toppings
make_pizza('pepperoni')                                         #first we pass a single argument
make_pizza('mushrooms' , 'green peppers' , 'extra cheese')      #multiple argumen t
'''
'''
def make_pizza(*toppings):                                          #Pass the arbitary arguments
    print("\n Making a pizza with the following toppings:")         #print statement as a head
    for topping in toppings:                                        #for loop for printing in next line
        print("-"+topping)                                          #print statement for 'for' loop
make_pizza('pepperoni')                                             #arbitary parameter
make_pizza('mushrooms' , 'green peppers' , 'extra cheese')          #arbitary parameter
'''

'''
#Mixing positional and arbitary argument

def make_pizza(size, *toppings):                                                    #pass the positional and arbitary arguments
    print("\n Making " +str(size) + "-inch pizza with the following toppings:")     #print statement for size and topping
    for topping in toppings:                                                        #'for' loop for taking positional argument
        print("-" + topping)

make_pizza(10 , "pepperoni")                                                        #passing parameter i.e size and single topping
make_pizza(12, "extra cheese", "mushrooms")                                         #passing parameter i.e size and arbitary topping
'''

'''
#Using An Arbitary Keyword
def build_profile(first , last , **user_info):                                                      #funct pass the arguments first , last and multiple dict
    profile = {}                                                                                    #create an empty dict
    profile['first name'] = first                                                                   #pass the key and argument in it as a value
    profile['last name'] = last
    for key, value in user_info.items():                                                            #create 'for' loop to store key , value of last arg(**user_info)
        profile[key] = value
    return profile                                                                                 #return profile stored in build_profile
user_profile = build_profile('albert' , 'einstein' , location = 'princetone' , field = 'physics')   #pass the first , last parameter and multiple key , value pairs in dictionary
print(user_profile)                                                                                 #print var(user_profile which contains "parametrs")
'''

#Storing Your Function In Modules
def make_pizza(size, *toppings):                                                    #pass the positional and arbitary arguments
    print("\n Making " +str(size) + "-inch pizza with the following toppings:")     #print statement for size and topping
    for topping in toppings:                                                        #'for' loop for taking positional argument
        print("-" + topping)


