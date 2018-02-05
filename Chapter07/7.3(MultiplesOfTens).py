num = input("Enter a number to check whether it is a multiple of ten or not? ")

num = int(num)

if num % 10 == 0:
    print("The number " + str(num) + " is a multiple of ten")
else:
    print("The number "+ str(num) + " is not a multiple of ten")