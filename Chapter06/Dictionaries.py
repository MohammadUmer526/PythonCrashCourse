'''
#simple dictionary
alien_0={'color':'green'}            #use curley bracket which takes dictionary{key:value}
print(alien_0['color'])
'''


'''
#multiple dictionaries
alien_0={'color':'green','points':5}      #multiple dictionaries
print(alien_0['color'],alien_0['points']) #use individual alien_color for other dictionary access

new_points = alien_0['points']
print("You just earned " + str(new_points) +" points!")
'''


'''
#Adding New Key-Value Pairs 
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['X_position']=0                      #commas must be use while declaing key name and in value for string
alien_0['Y position']=250
print(alien_0)
'''

'''
#Starting with an Empty dictionary

alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)
'''


'''
#Modifying Values in Dictionary
alien_0={'color':'green'}
print("The alien is: " + alien_0['color'] + ".")                #to print dictionary value dictionary

alien_0['color']='yellow'
print("The alien is now: " + alien_0['color'] + ".")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print("Original position of x: " +str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_imcrement = 1
elif alien_0['speed'] == 'medium':
    x_imcrement = 2
else:
    #the fastest alien such as speed is greater than medium
    x_imcrement = 3
alien_0['x_position'] = alien_0['x_position'] + x_imcrement

print("New poisition of x: "+ str(alien_0['x_position']))
'''

'''
#Removing Key-Value Pairs

alien_0={'color':'green', 'points' : 5 }
print(alien_0)

#del [alien_0['points']]
print(alien_0)
'''

'''
#A Dictionary of Similar Objects
favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}
print("Srah favourite languages is: " + favorite_languages['sarah'].title() + ".")
'''

'''
#Looping through All Key-Value Pairs
user_0={'username':'efermi',                #dictionary containing key and values
        'first_name':'enrico',
        'last_name':'fermi'}

for key, value in user_0.items():           #dict(user_0)'s all item stores in var key(key of an element) , var value(value of an element)
    print("\nKey: "+ key)                   #print the value of var key
    print("Value:" + value)                 #print the value of var value
'''

'''
#favorite languages continue..

favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}
for name, languages in favorite_languages.items():
    print(name.title()+ "'s favorite languages is: " + languages.title()+ ".")
'''

'''
#Looping through All the Key in a Dictionary
#key()function is used when we do not need work with all "values".

favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}
for names in favorite_languages.keys():
    print(names.title())
'''

'''
friends=['phil','sarah']
favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + sorted(name.title()) ,"I see your favorite language is " + favorite_languages[name].title( ) + "!")           #dict[name] is used to call dict and name is use as a "kery", we use only just because satifying "if" statement.
'''


'''
#Looping through a Dictionary's Keys in Order
#use sort() func

favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}

for name in sorted(favorite_languages.keys()):
    print(name.title()+" thank you for taking the poll!")
'''

'''
#Looping Through All Values Dictionary
favorite_languages={'jen':'python',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}
print("The following languages have been mentioned:")
for language in favorite_languages.values():            #.values() will give all the values in dictionary
    print(language.title())
'''

'''
#Looping Through a Dictionary's Value in Order

favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}
for language in sorted(favorite_languages.values()):        #sorted() will sort the all values in dictionary because we use value() func for values in dictionary
    print(language.title())
'''


'''
#Nesting

alien_0={'color':'green','points':5}            #dict 1
alien_1={'color':'yellow','points':10}          #dict 2
alien_2={'color':'red','points':15}             #dict 2
aliens = [alien_0,alien_1,alien_2]              #list which contains all dictionaries

for alien in aliens:
    print(alien)

'''

'''

aliens = []

for alien_number in range(30):
    new_alien={'color':'yellow','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("....")
print("Total number of aliens: "+(str(len(aliens))))

'''

'''
#change first three elements's color
aliens = []                                                     #creates empty list

for alien_number in range(30):                                  # use range func for iteration i.e 30
    new_alien={'color':'green','points':5,'speed':'slow'}       #create dictionary called "new_alien".
    aliens.append(new_alien)                                    #appending the dict(abive) in alien.

for alien in aliens[0:3]:                                       #check only first three element in list
    if alien['color'] == 'green':                               #check for condition
        alien['color'] = 'yellow'
        alien['points'] = 5
        alien['speed'] = 'medium'

for alien in aliens[0:5]:                                       #use slice to take only first five elements in list
    print(alien)                                                #print alien(above)
print("....")
print("Total number of aliens: "+(str(len(aliens))))            #show the total num of aliens(range()30)
'''



'''
#elif in above condition

aliens = []                                                            #create empty list

for alien_number in range(0,30):                                       #use range func for iteration
    new_alien = {'color' : 'yellow', 'points' : 5, 'speed' : 'slow'}   #create new dict
    aliens.append(new_alien)                                            #appending new dict in list(aliens)

for alien in aliens:
    if alien['speed'] == 'slow':
        alien['color'] = 'green'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:3]:
    print(alien)
print("The total num of alien: " + str(len(aliens)))
'''

'''
#A list in a Dictionary
pizza = {'crust' : 'thick', 'toppings' : ['mushrooms','extra cheese'], }

print("You ordered a " + pizza['crust'] + " -crust pizza" + " with the following topping:" )

for topping in pizza['toppings']:
    print("\t"+topping.title())
'''

'''
favorite_languages = {'jen' : ['python' , 'java'], 'sara' : ['c'], 'edward' : ['ruby','go'], 'phil' : ['python','haskell']}   #dict in which value is key

for k, v in favorite_languages.items():                                                                                       #loop in which key, value of above dict are stored using items()
    print(k.title()+ "'s " + " favorute languages are: ")                                                                     #printing keys in dict
    for iv in v:                                                                                                               #inner loop for printing value of each key
        print(""+iv.title())
'''

'''
#Dictionary in a Dictionary

users = {'ainstein' : {'f_name' : 'albert' , 'l_name' : 'einstein' , 'location' : 'princeton'} , 'mcurie'  : {'f_name' : 'marie' , 'l_name' : 'curie' , 'location' : 'paris'} , }
for user_name , user_info in users.items():
    print("Username: " + user_name.title())
    full_name = user_info['f_name'] + " " + user_info['l_name']
    location = user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+ location.title())
'''