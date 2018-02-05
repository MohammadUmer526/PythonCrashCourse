#l_person_1=

#l_person_2 =

#l_person_3 =

people = [{'first name: ':'Muhammad','last name: ':'Ali','age: ':'22','city: ':'Karachi',} ,  {'first name: ' : 'Muhammad' , 'last name: ' : 'Umer' , 'age: ' : 18 , 'city: ' : 'Lahore'}  , {'first name: ' : 'Muhammad' , 'last name: ' : 'Zubair' , 'age: ' : 20 , 'city: ' : 'Peshawar'} ]
#store all dictionaries in a list(above)

print("Dictionary 1in a list have the following information:\n")        #a print statement for all elements in dictionary 1
for k,v in people[0].items():                                           #loop in which k,v are two variables getting key and value from list index'0'
    print(""+str(k).title()+str(v).title()+"\n")                        #printing key and value of dict 1 title due to "title()"recpectively


print("Dictionary 2 in a list have the following information:\n")       #a print statement for all elements in dictionary 2
for k,v in people[1].items():                                           #loop in which k,v are two variables getting key and value from list index'1'
    print(""+str(k).title()+ str(v).title()+"\n")                       ##printing key and value of dict 2 title due to "title()"recpectively

print("Dictionary 3 in a list have the following information:\n")       #a print statement for all elements in dictionary 3
for key, value in people[2].items():                                    #loop in which k,v are two variables getting key and value from list index'2'
    print(""+str(key).title()+str(value).title())                       #printing key and value of dict 3 title due to "title()"recpectively