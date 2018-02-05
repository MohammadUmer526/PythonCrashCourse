favorite_places = {'key_1' : 'mecca' , 'key_2' : 'madina' , 'key_3' : 'sham'}

friend_1 = input("Enter your favorite place: ")                                                                      #prompt user for input
friend_2 = input("Enter your favorite place: ")                                                                      #prompt user for input

favorite_places = {'saad' : 'mecca' , 'zaid' : 'madina' , 'asad' : 'sham' , 'ali ' : friend_1 ,'umer ' : friend_2}   #dict in which last two keys are prompting(user input)

for re, ve in favorite_places.items():                                                                               #loop re, ve are keys and values respectively
    print("Friend's name is "+re.title()+" his favorite place is "+ve.title())                                       #printing the fav places and friends names
