class Users():
    def __init__(self, f_name, l_name, religion, age, city):
        self.f_name = f_name
        self.l_name = l_name
        self.religion = religion
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        long_name = "Name: " + self.f_name.title() + " " + self.l_name.title() + "\nReligion: " + self.religion.title() + "\nAge: " + str(
            self.age) + "\nCity: " + self.city.title() + "\n"
        return long_name # returning the name of a user

    def greet_users(self):
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_attempts(self):
        self.login_attempts = 0


class Admin(Users):
    def __init__(self, f_name, l_name, religion, age, city, prvl_list):
        super().__init__(f_name, l_name, religion, age, city)
        self.prvl_list = prvl_list

    def show_privileges(self): # method for admin's right(defined in a list)
        print("The admin has the following rights: ")
        for ab in self.prvl_list:
            print(ab.title())


adm_user = Admin('Muhammad', 'Ali', 'Islam', 22, 'Karachi', ['it can add post', 'it can delete post', 'it can be user'])
print(adm_user.describe_user()) # print the user method which is defined in parent class
adm_user.show_privileges()      # print the method 'show_privileges()' that will show rights of admin(defined in a list)
