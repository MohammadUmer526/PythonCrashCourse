file_loc = 'C:\\Users\Muhammad Umer\\Desktop\\10.5.txt'

flag = True # create a flag and set it 'True'
print("Enter q to quit.") # print to statement to tell user press 'q' to terminate the process
while flag: # use 'while' and flag which is 'True'
    ac = input("Why do you like programming?\n")

    with open(file_loc, 'a') as file_object:  # use func'open' to 'append' in file
        file_object.write(ac+"\n")      # appending input in file

    if ac == 'q':  # use 'q' for terminate the process
        flag = False # if user input 'q' then 'flag' values becomes 'False'

    # check your file which created at the top of the program 'file_loc', for appending 'strings'.
