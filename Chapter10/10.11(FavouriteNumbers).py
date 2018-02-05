import json
fielname = '10.11.json'

fav_num = int(input("What is your favourite number?"))
with open(fielname , 'w') as f_obj:
    json.dump(fav_num,f_obj)
    print("We will remember your favourite number, "+str(fav_num) + "!")


with open(fielname) as f_obj:
    num = json.load(f_obj)
    print("I know you favourite number! It's, "+str(num))

