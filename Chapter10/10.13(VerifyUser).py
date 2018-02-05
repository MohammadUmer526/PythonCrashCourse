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
    if username: # check the username
        correct = input("Are you " +username + "? (y/n)") # prompt for user name
        if correct == 'y':
            print("Welcome back, " + username+ "!")

        else: # if no the call func'greet_new_username' for adding new user
            username = get_new_username()
            print("We will remember you when you comeback, " + username + "!")

    else:
        username = get_new_username()
        print("We will remember you when you comeback, "+username+ "!")
greet_user()