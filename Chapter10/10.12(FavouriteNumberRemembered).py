import json
fielname = '10.12.json'
try:
    with open(fielname) as f_obj:
     number = json.load(f_obj)
except FileNotFoundError:
    number = input("Whats is your favourite number?")
    with open(fielname,'w') as f_obj:
        json.dump(number,f_obj)
        print("We will remember your number.")

else:
   print("I know  your favourite number! It's " + str(number)+ ".")