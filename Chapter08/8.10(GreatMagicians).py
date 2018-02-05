def show_magicians(org_list):
    print("")
    for lists in org_list:
        print(lists.title())
    return lists
list=['john' , 'clark' , 'stuart' , 'anderson']                     #create a list
show_magicians(list)                                                #pass the argument(list in it)

print("\n")
def make_great(great_magician_lists):                      #declare a new function and pass argument magician_lists
    for magician_list in great_magician_lists:                      #use for loop for eaccessing each element ij list
        print("Great "+magician_list.title())                       #printing the message

    return magician_list
make_great(list)                                               #pass the parameter"list"