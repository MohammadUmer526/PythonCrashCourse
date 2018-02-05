prompt = "How old are you?"
prompt+= "\nEnter quit when you are finished"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age =int(age)

    if age < 3:
        print("Your ticket is free")
    elif age > 3 and age < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
