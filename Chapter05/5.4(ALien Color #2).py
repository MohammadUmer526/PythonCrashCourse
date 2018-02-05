#alien_color=input("Enter alien color: ")
'''
if alien_color=="Green":
    print("Yous just earned 5 points!")
elif alien_color!="Green":
    print("You earned 10 points!")
'''

'''
if alien_color=="Green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")
'''

'''
if alien_color=="Green":
    print("You earned 5 points!")
elif alien_color=="Yellow":
    print("You earned 10 point!")
elif alien_color=="Red":
    print("You earned 15 points!")
else:
    print("Color not identified")
'''

'''
available_toppings = ['mushrooms', 'olives', 'green pepper','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
     if requested_topping=="Mushrooms":
         print("Sorry we are ou og green pepper")
     else:
            print("Adding "+requested_topping+".")
'''

'''
#my solution
myfriends=['Saad','Zaid','Asad','Ali','Faizan','Ahmed','Haya','Usman','Bilal']
newfired=['Ahmed','Asad','Ali']
#for newfirend in myfriends:
if myfriends=="Ahmed" or "Ali" or "Asad":
    print("These friends names starts with A: ",newfired)
else:
    print("No firends name starts with A")
'''

myfriends=['Saad','Zaid','Asad','Ali','Faizan','Ahmed','Haya','Usman','Bilal']
newfriends=[]
for myfriend in myfriends:              # for loop for iteration(checking every element in,ist)
    if myfriend[0]=='A' or 'a':                # must be start from '0' and check with first letter
        newfriends.append(myfriend)     # appending every element which starts from 'A'
print(newfriends)                       # print the elements which starts with 'A'
print(newfriends)                       # print the elements which starts with 'A'



