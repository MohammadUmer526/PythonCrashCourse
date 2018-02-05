file_name = 'C:\\Users\Muhammad Umer\\Desktop\\10.4.txt'

while True: # create a 'while loop' and create a flag as true
    ab = input("Enter your name: ") # prompt for user input
    print("Grreting "+ab)    # printing greeting message to each user(multiple times ask for input due to 'while' loop)
    with open(file_name, 'a') as file_object: # use open func in which passes arguments of file name and 'a'(to append)
        file_object.write(ab+"\n") # 'append' every input into a new line
