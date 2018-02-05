laptops=['hp elitebook', 'air boo 2017', 'Dell 6470', 'Lenovo i3', 'Compaq 2316']
'''print(laptops)
print(laptops[0])
print(laptops[4])
print(laptops[1].title())
print(laptops[3].lower()'''

'''

# use in meesage

message = "My laptop is " + laptops[0].title() 
print(message)

'''

'''
# access list with negative index

print(laptops[-3])   # in negative index just count with back element's index and add '-' for indexing

'''


'''
#adding element

motorcycles.append('Ducati')

print(motorcycles)

'''

'''

#insert element at any position

motorcycles.insert(1,'Ducati')  #it will insert at the position of 'Honda 150' and 'Honda 150' position ' will be increased by 1

print(motorcycles)

'''
'''
#deleting an item

del motorcycles[1]
print(motorcycles)
'''

'''

#pop methid

motorcycles.pop()   #last element will be deleted
print(motorcycles)



motorcycles.pop(0) #delete 0th element as we gave position of an element
print(motorcycles)

'''

''' 

remove method
motorcycles.remove('Honda 150') #it will remove first occurance of entered parameter(Honda 150), if it occurs more than 1 time the we have to use loop
print(motorcycles)

'''

# organizition list

#print(laptops)

'''
#sort()

laptops.sort() #it will sorted list in an alphabetically order and this changes will be applied after using sort()
print(laptops)
print(laptops)
'''

'''
#sorted()

print("This is the list of my laptops "+str(laptops))
print("This is sorted list of my laptops "+str(sorted(laptops)))
print("After sorted() fuction, it remains sameas original")
print(laptops)
'''

'''
# reverse a list

laptops.reverse()
print(laptops)  #we have to set reverse() opt before printing it ohterwise it will show "None"

'''

'''

#print the length of a list
print(len(laptops))

'''

