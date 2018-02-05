cat = {'kind: ' : 'street' , 'owner: ' : 'umer' }
dog = {'kind: ' : 'safety' , 'owner: ' : 'ahmed'}
lion = {'kind: ' : 'jungle' , 'owner: ' : 'saad'}

my_list = [ cat , dog , lion]

print("The first element of list is Cat which have the following information:")
for a,b in my_list[0].items():
    print(str(a).title()+ str(b).title())

print("\nThe second element of list is Dog which have the following information:")
for x , y in my_list[1].items():
    print(str(x).title()+str(y).title())

print("\nThe second element of list is Dog which have the following information:")
for r , s in my_list[2].items():
    print(str(r).title()+str(s).title())
