'''

with open('pi_digits.txt') as file_object: # open is a func which takes one argument i.e 'file name' it will open 'as' 'file_object'
    contents = file_object.read() # take a string var 'contents' and assigning it 'file_object' and 'read()' is used to read all data in it.
    print(contents.rstrip()) # print the 'contents'
'''

'''

# Absolute File Path

file_path = 'D:\Data Science & AI\Welcome.txt' # store the location of a file in var 'file_path'
with open(file_path) as file_object:    # use open func and pass 'file_path' a s a argument on it and assign to 'file_object'
    contents = file_object.read()   # Read file from 'file_object' and assign it into var 'contents'
    print(contents)                 # print the 'contents' i.e 'File'
'''

'''
# Read Line By Line

file_path = 'D:\Data Science & AI\Welcome.txt'  # give file path in a var 'file_path'

with open(file_path) as file:  # use open func and pass argument file path in it
    for xy in file:  # use for loop to print file line by line and assign 'file' in 'xy'
        print(xy)  # print the file, it will print in line by line

'''

'''
# Making A List of Lines from A File

file_path = 'D:\Data Science & AI\Welcome.txt' # give a path of a file in var 'file_path'
with open(file_path) as object:         # use open func and pass 'file_path' a s a argument on it and assign to 'object'
    lines = object.readlines()          # use func'.readlines()' which reads every line of object(file located in it)

for line in lines:              # use loop to print individual line
    print(line)                 # print var 'line'
'''

# Working with a File's Content
'''
file_path = 'D:\Data Science & AI\Welcome.txt' # give a path of a file in var 'file_path'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string +=line.rstrip()

print(pi_string)
print(len(pi_string))
'''

# Large Files: One million digits
'''
filename = 'C:\\Users\\Muhammad Umer\\PycharmProjects\\pi_million.txt'  # give a path of file in var

with open(filename) as file:                    # use func 'with ' to open a file(var) and change it's to 'file'
    lines = file.readline()     # use read func to read lines

pi_string = ''      # declare a empty var 'pi_string to contain digits of file'
for line in lines:  # create a loop 
    pi_string += line.strip()  # allocate file all digits in empty var(pi_string)

print(pi_string[ : 52] + "....") # print only 0 to 52 digits using slice
print(len(pi_string)) # print the 'length' of digits that we print by using 'slice method'
'''

# Is Your Birthday Contained in PI
'''
file_path = 'D:\Data Science & AI\Welcome.txt' # give a path of a file in var 'file_path'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in this text file!")
else:
    print("Your birthday does not appear in this file")
'''

# Writing To A File

# Writing To An Empty File
'''
file_name = 'C:\\Users\Muhammad Umer\\Desktop\\pyt.txt' # give a path of a file which you want to create

with open(file_name, 'w') as file_object:   # use open func which takes two argument file name and 'w' denotes to
    # write mode.
    file_object.write("I Love Programming!") # use write method to write a text in above 'file_name' file.

    # It will only write 'string value' to write numerics value we must use 'str' method and you can see the output
    # in a file which is stored in above location 'file_name'

# Writing Multiple Lines

with open(file_name, 'w') as file_object:   # use open func which takes two argument file name and 'w' denotes to
    # write mode.
    file_object.write("I Love Programming.") # use write method to write a text in above 'file_name' file
    file_object.write(" I will use to create AI apps.")  # use write method to write a new text in above 'file_name' file
'''

# Appending to A File
# To Appened A File we use 'a' append mode
'''
file_name = 'C:\\Users\Muhammad Umer\\Desktop\\pyt.txt' # give a path of a file which you want to create

with open(file_name, 'a') as file_object:
    # append mode
    file_object.write("\nI am in chapter 10 of 'Python Crash Cours'") # append a new line in above file
'''

# Exceptions

# Handling The ZeroDivisionError Exception
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero")
'''

# Using Exception To Prevent The Crash
'''
print("Give me a two numbers and I will divide them.")
print("Press q to exit.")

while True: # create a 'While loop' and set as 'True'

    first_num = input("\nEnter a first number: ") # prompt user to input number 1
    if first_num == 'q': # if user want to quit so he can enter 'q'
        break # it will terminate the process

    secound_num = input("\nEnter secound number: ") # prompt user to input number 2
    if secound_num == 'q':
        break

    try: # try block
        answer = int(first_num) / int(secound_num) # where error can occur

    except ZeroDivisionError: # except block where we define which type of error it is.
        print("You cannot divide by zero.")

    else: # else block is used if there is no error so program will execute as it written
        print(answer)
'''

# Handling The FileNotFound Exception
'''
file_name = 'C:\\Users\Muhammad Umer\\Desktop\\10.32.txt' 
with open(file_name) as f_obj: 
    content = f_obj.read()
    print(content)


# To prevent above programm error(File Not Found), we use try-except-else block

file_name = 'C:\\Users\Muhammad Umer\\Desktop\\10.32.txt' # give a path of file(may be it can be wrong)

try: # create a 'try' block in which the part of program we write where error can occur
    with open(file_name) as f_obj: # use func'open' to open a file
        content = f_obj.read()
        print(content)
except FileNotFoundError: # use func 'except' to prevent error(File Not Found)
    msg = "Sorry, the file " + file_name + " is not in the directory" # create a var message if error occurs
    print(msg) # print var 'msg'
    
    # you can also use 'else' block(print the file) if there is no error but it is not necessary.
'''

# Analyze The Text
'''
file_name = 'C:\\Users\\Muhammad Umer\\Desktop\\alice.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist"
    print(msg)

else:
    words = contents.split()  # use 'split' method which which create a list and allocate all the words in a that list
    #  and assign it in a new var'words'
    num_words = len(words)  # create a new var 'num_word' and pass the length 'len' of the list(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")  # print the length of the words in a
    # file.
'''

# Working With Multiple Files
'''
def count_words(filename):  # we just create a func'count_words'(pass the argument and parameter) and indented previous code in it
    """Count the approximate number of words in each line"""
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = " Sorry, the file " + filename + " does not exist in the directory."
        print(msg)
    else:
        words = content.split()
        total_words = len(words)
        print("The file, " + filename + " has about " + str(total_words) + " words in it.")


filename = 'C:\\Users\\Muhammad Umer\\PycharmProjects\\pi_million.txt'
count_words(filename)
'''

# Counting multiple file's words
'''
def count_words(file_names):

    try:
        with open(file_names) as f_object:
            content = f_object.read()

    except FileNotFoundError:
        msg = "Sorry the file, " + file_names + " does not exost."
        print(msg)

    else:
     words =  content.split()
     total_words = len(words)
     print("The file, " + file_names + " chas about " + str(total_words) + " in it.")

file_names = ['C:\\Users\Muhammad Umer\\Desktop\\10.4.txt' , 'file_1eetxt' ,'C:\\Users\Muhammad Umer\\Desktop\\10.3.txt' , 'C:\\Users\\Muhammad Umer\\PycharmProjects\\pi_million.txt'] 

# create a list above and allocate multiples file addresses

for file_name in file_names: # create a loop to access each file one by one and allocate that file in a new var'file_name'

    count_words(file_name) # pass the parameter 'file_name' which contains all the addresses of each files
 '''

# Failing Silently

'''

def count_words(file_names):
    try:
        with open(file_names) as file_obj:

            content = file_obj.read()


    except FileNotFoundError:
        pass # we use func'pass' which will ignore exception and process to next execution

    else:
        words = content.split()
        tot_words = len(words)
        print("The file, " + file_names + " has about" + str(tot_words) + " words in it.")

list_files = ['C:\\Users\Muhammad Umer\\Desktop\\10.4.txt' , 'file_1eetxt' ,'C:\\Users\Muhammad Umer\\Desktop\\10.3.txt' , 'C:\\Users\\Muhammad Umer\\PycharmProjects\\pi_million.txt']

for list_file in list_files:
    count_words(list_file)
    
'''

# Storing Data

# Using json.dump() and json.write()
'''
import json # import json

numbers = [2, 3 , 5, 7, 11, 13] # create a list(piece of information)

fillename = 'numbers.json' # file name

with open(fillename, 'w') as f_obj: # use func 'open'
    json.dump(numbers , f_obj) # use func 'json.dump()'  to store information

'''

# Write json.load()
'''
import json  # import json library

file_name = 'numbers.json'  # give a file path
with open(file_name) as f_obj:  # use func 'open'
    numbers = json.load(f_obj)  # use method 'json.load()' to load the information stored in numbers.json & store it
    # in var 'numbers'

print(numbers)  # print var'numbers'
'''

# Saving And Reading User-Generated Data
'''
import json

username  = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username , f_obj)
    print("We will remember you when you come back, " + username + "!")
'''

# Greets username
'''
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!" )
'''

# Combine above programs
'''
import json

filename = 'username1.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
         json.dump(username,f_obj)
         print("We will remember yo when comeback, " +username + "!")

else:
    print("Welcome back, " + username + "!")
'''

# Refactoring
'''
import json

def greet_user(): # define a func'greet_user()'
    filename = 'username2.json' # create a file in directory in a 'Python Workspace'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename, 'w')as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you comeback, " + username + "!")

    else:
        print("Welcome back, " + username + "!")
greet_user()
'''

# Two func
'''
import json

def get_stored_name():
    fielname = 'username4.json'

    try:
        with open(fielname) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_name()

    if username:
        print("Welcome back, " + username+ "!")

    else:
        username = input("What is your name?")
        filename = 'username4.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We will remember you when you comeback, "+username+ "!")
greet_user()
'''

# Adding new user by prompting
'''
import json

def get_stored_name(): # use for retrievong the info, if a username exist otherwise it is return 'None'
    fielname = 'username4.json'

    try:
        with open(fielname) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(): # responsible for load and store 'username'
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename , 'w') as f_obj:
        json.dump(username,f_obj)

    return username


def greet_user():  # it either welcome a stored user or greet a new user
    username = get_stored_name()

    if username:
        print("Welcome back, " + username+ "!")

    else:
        username = get_new_username()
        print("We will remember you when you comeback, "+username+ "!")
greet_user()
'''


