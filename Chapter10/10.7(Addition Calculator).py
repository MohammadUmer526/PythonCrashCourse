print("Press q to quit")

while True:
    try:
        first_num = input("Enter first number: ")  # prompts user for input either text(later convert into int) or 'q' for exit'

        if first_num == 'q':
            break
        first_num = int(first_num) # converting input into string because user can give 'q' for exit which cannot be quit because it reads as text

        second_num = int(input("Enter second number: "))

        if second_num == 'q':
            break

        second_num = int(second_num)
    except ValueError:
     print("Sorry, pleas enter a number")

    else:
        answer = int(first_num) + int(second_num)  # adding two numbers and assign it into a var 'answer'
        print("The result of two number is: " + str(answer) + "\n" )  # print the result 'answer'