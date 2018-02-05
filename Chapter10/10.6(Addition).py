try:
    first_num = int(input("Enter first number: "))  # prompts user for input and convert it into 'int'
    second_num = int(input("Enter second number: "))
except ValueError:  # define 'except' and tells 'ValueError' if 'text' is input.
    print("Sorry, Please enter a number!")
else:
    answer = int(first_num) + int(second_num)  # adding two numbers and assign it into a var 'answer'
    print("The result of two number is: " + str(answer))  # print the result 'answer'
