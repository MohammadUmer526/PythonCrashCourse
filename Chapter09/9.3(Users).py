class Users():
    def __init__(self,f_name,l_name,religion,age,city):
        self.f_name= f_name
        self.l_name = l_name
        self.religion = religion
        self.age = age
        self.city = city

    def describe_user(self):
        print("First Name: " + self.f_name.title())
        print("Last Name: " + self.l_name.title())
        print("Religion: " + self.religion.title())
        print("Age: " + str(self.age))
        print("City: " + self.city.title() + "\n")


    def greet_users(self):
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + "!")


user_1 = Users('Muhammad' , 'Umer' , 'Islam' , 22 , 'karachi')
user_2 = Users('Muhammad' , 'ALi' , 'Islam' , 24 , 'lahore')
user_3 = Users('Muhammad' , 'Saad' , 'Islam' , 16 , 'peshawer')

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

user_1.greet_users()
user_2.greet_users()
user_3.greet_users()

