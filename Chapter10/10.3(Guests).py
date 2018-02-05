file_loc = 'C:\\Users\Muhammad Umer\\Desktop\\10.3.txt'

ab = input("Enter your name: ")

with open(file_loc, 'w') as file:
    file.write(ab) # write 'ab' user input in above file

