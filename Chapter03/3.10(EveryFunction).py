languages=['Java','Swift','Python','C','C++','Ruby','Perl','COBOL']

'''

#adding an element by append

print(languages.append('NodeJs'))   #it will add 'Node Js' at the end of the list
print(languages)

'''

'''

#for adding element at any position

languages.insert(3,'Pascal')  #it will add 'Perl' at the place of 'C' and C's index is increased by one that will be '4'
print("New List: \n" +str(languages))  #use str to convert list into string

'''

'''

#to remove item through index and deafult remove of an element

languages.pop()                            #it will automatically remove last element of lis
print(languages)
languages.pop(3)                           #it will remove 4 element
print(languages)

'''

'''

#to remove itme by using remov function which only takes value not index

languages.remove("Perl") # it will remove by value, in this case it is "Perl"
print(languages)

'''

'''

#to delete item by using del function
del languages[3] #it will delete by index, in this "C"
print(languages)
print(languages)

'''

'''

#sorting use sort

languages.sort()  #firs we have to declare sort method
print("Sorted list is: \n\t\t\t" +str(languages))  #it will sort the list permanently and use str for parsing

'''

'''

#sort using sorted

print(sorted(languages))   #it wil sorted the list for temporary base that's why we don't need to declare the of "sorted" before printing it

'''

'''

#reverse the list

languages.reverse()
print(languages)  #it will reverse the list for temporary base

'''



#find the length of thelist

print("Length of the list is: " +str(len(languages)))   #it will give the length and we cannot declare the length function before using or printing it, it shows length only when we need(printing) and also use str for converting it

