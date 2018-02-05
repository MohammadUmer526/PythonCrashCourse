friends_fav_num={'Umer' : 18 ,'Ali' : 19 , 'Saad' : '16' , 'Zaid' : 24 , 'Asad' : 26 , }                    #dictionary

friend_1 = str(input("Umer, enter your favorite number: "))                                                 #prompt user for input i.e friend and goes on till friend 5
friend_2 = str(input("Ali, enter your favorite number: "))
friend_3 = str(input("Saad, enter your favorite number: "))
friend_4 = str(input("Zaid, enter your favorite number: "))
friend_5 = str(input("Asad, enter your favorite number: "))

print("\n")

for k , v in friends_fav_num.items():                                                                       #loop for access list using "items()" and k, v for storing 'keys' and 'values'
    if k == 'Umer':
        print("Friend 1's name is " + str(k) + " his favorite numbers are " + str(v)+ " ," + friend_1)      #checking for user name then insert modify number(input) for all users i.e(1 to 5)
    elif k == 'Ali':
        print("Friend 2's name is " + str(k) + " his favorite numbers are " + str(v) + " ," + friend_2)
    elif k == 'Saad':
        print("Friend 3's name is " + str(k) + " his favorite numbers are " + str(v) + " ," + friend_3)
    elif k == 'Zaid':
        print("Friend 4's name is " + str(k) + " his favorite numbers are " + str(v) + " ," + friend_4)
    elif k == 'Asad':
        print("Friend 5's name is " + str(k) + " his favorite numbers are " + str(v) + " ," + friend_5)