names=[]

if names in names:
    print("We need to find sone users!")
else:
    print("")
usernames = input("Enter an username:")
if usernames=='Admin':
    print("Hello "+str(usernames)+" would you like to see a status report?")
elif usernames in names:
    print("Hello "+str(usernames)+" thank you for loggig in again")

