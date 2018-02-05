class Users():
    def __init__(self,f_name,l_name,religion,age,city):
        self.f_name= f_name
        self.l_name = l_name
        self.religion = religion
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: " + self.f_name.title())
        print("Last Name: " + self.l_name.title())
        print("Religion: " + self.religion.title())
        print("Age: " + str(self.age))
        print("City: " + self.city.title() + "\n")

    def greet_users(self):
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + "!")

    def increement_login_attempts(self):
        self.login_attempts += 1

    def reset_attempts (self):
        self.login_attempts = 0


user = Users('Muhammad' , 'Umer' , 'Islam' , 22 , 'karachi')

user.describe_user()


user.greet_users()

print("***Making Log-In Attempts***")
user.increement_login_attempts()
user.increement_login_attempts()
user.increement_login_attempts()
print(" Log in Attempts: " + str(user.login_attempts))

print("Resulting log in attempts..")
user.reset_attempts()
print("Log In attempts: " + str(user.login_attempts))