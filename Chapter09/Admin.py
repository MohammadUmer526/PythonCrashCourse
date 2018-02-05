from Classes import Users

class Admin(Users):
    def __init__(self, f_name, l_name, religion, age, city):
        super().__init__(f_name, l_name, religion, age, city)
        self.prvl_list = Privileges()  # calling the class 'Privileges' and assigning it to 'self.prvl_list'


class Privileges():
    def __init__(self, privileges=['it can add post', 'it can delete post', 'it can be user']):
        self.privileges = privileges

    def show_privileges(self):  # method for admin's right(defined in a list)
        print("The admin has the following rights: ")
        for ab in self.privileges:
            print(ab.title())
# for further steps go to my_admin.py