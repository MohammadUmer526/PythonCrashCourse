age=int(input("Enter the age: "))
if age < 2:
    print("The person is baby.")
elif age > 1 and age < 4:
    print("The person is toddler.")
elif age > 3 and age < 13:
    print("The person is baby.")
elif age > 12 and age < 20:
    print("The person is teenager.")
elif age > 19 and age < 65:
    print("The person is adult.")
elif age > 64:
    print("The person is elder.")
