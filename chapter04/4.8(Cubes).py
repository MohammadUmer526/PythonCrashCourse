listcube=[]
for cube in range(1,11):
    abc=cube**3              #
#or, listcube.append(cube**2) do not need to declare "abc = cube**3"
    listcube.append(abc)
print(listcube)            #outside the loop otherwise it will print in a order


