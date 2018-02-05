magicians=['alice','daivid','john','santner']
'''
for magician in magicians:
 print(magician)

for value in range(1,6):
    print(value)

for valuelist in list(range(1,4)):
    print(valuelist)
'''
tuple=('a','b','c')  #use where program must not change by user input

'''print(tuple)
mylist=['a','b','c']
print(mylist)
mylist[1]='B'
print(mylist.insert(1,"B"))
print(mylist)
'''
#a='1'
#b='2'
#tuple=a,b
#print(tuple)
dimension=(0,250)
#print(dimension)
#dimension[0]=250
#print(dimension)

#for dimensions in dimension:
#   print(dimensions)

'''print("Original dimensions: \n")
for dimensions in dimension:
    print(dimensions)

dimension=(100,400)
print("\nModified Value:\n")
for dimensions in dimension:
    print(dimensions)

def myfunc():
     return(1,2,3)
print(myfunc())

first,second,third=myfunc()
print(first)

tuple=('a','b','c')

tuple=11,12,13
print(11)
'''

'''
#using range() function
for value in list(range(1,5)):
    print(value)
'''

#using range() function for list

'''
numberlist= list(range(1,6))
print(numberlist)

'''

'''
#ysing range func for even number

even_number = list(range(2,11,2)) #staring number (2), limitation (11) 11 - 1 10 in this case.
print(even_number)

#using range function for odd number
odd_number = list(range(1,10,2))
print(odd_number)
'''
'''
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
'''

'''
cubic=[]
for value in range(11,21):
    cube=value**2
    cubic.append(cube)
print(cubic)
'''
'''
squares=[]
for value in range(1,11):
    squares.append(value**2)
    print(squares)
'''
'''
sq=[]
for val in range(1,15):
    #sqr=vl**2
    sq.append(val**2)
    print(sq)
'''
'''
#Simple Statistics With a List of Numbers

digits=[1.1,2.4,3,4,5,6,7]  #it will perform some functions
print(min(digits))          # show min digit
print(max(digits))          # show max digit
print(sum(digits))          #show sum of the list

#Simple Statistics with a List of Names

names=['Umer','Haya','Faizan']
print(min(names))       # it shows min digit by the FIFO alphabetically order in this case 'Faizan' because 'F' comes before 'U' and 'H'
print(max(names))       # it shows max digit by the LIFO alphabetically order in this case 'Umer' because 'U' comes after 'F' and 'H'

'''

'''
#List Coprehension(Previoues Code in one Line)

squares=[value**2 for value in range(1,10)]
print(squares)


mult=[odd**3 for odd in range(1,10,2)]
print(mult)

'''

'''
#slicing a list
players=['charles','martina','michael','florence','eli']
print(players[0:5])                             #it will start '0' index end with n-1


print(players[:-3])

'''

'''
#looping through slicing

games=['cricket','football','hockey','table tennis','snooker']
print("\nHere is the list of games: \n")
for gme in games[0:6]:
    print(gme.title())
'''

'''

#copyng a list

my_foods=['Pizza','Pasta','Burger','Sandwich']
friends_foods=my_foods[:]
my_foods.append('Icecream')
print("My foods: ",my_foods)
print("My friend's food: ",friends_foods)

my_foods.insert(0,"Tikka")  #inserting an element by using insert func.
print("My foods: ",my_foods)


'''
'''
#tuple

dimension=(50,250)
print(dimension[0])
dimension[0]=25
# print(dimension[0])             #give error because tuple cannot be changed

'''
dimension = (25,50,100)
#looping through all element
print("Dimension are: \n")
for dim in dimension:
    print(dim)

#Writing over a tuple

dimension = (200,250)
print("\nModified dimensions: ")
for dim2 in dimension:
    print(dim2)

#styling a code is last topic of this chapter