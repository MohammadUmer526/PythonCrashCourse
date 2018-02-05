# Creating and Using A Class
'''
class Dog():
    """A Simple Attempt To A Dog Module"""

    def __init__(self, name, age):
        "Initialize name and age attributes."

        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " is rolled over!.")


# Making An Instance From A Class

my_dog = Dog('wille', 6)
print("My dog name is " + my_dog.name.title() + "")
print("It's age is " + str(my_dog.age) + " years old")

# Calling Methods

my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instance
your_dog = Dog('lucy', 3)
print("\nMy second dog's name is " + your_dog.name.title())
print("It's age is " + str(your_dog.age) + " years old")
your_dog.sit()
your_dog.roll_over()

'''

# Working With Classes And Instance
import self as self

"""
class Car():
    # A Simple attempt to represent

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

"""

'''
class Car():
    """ A Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''

# Modifying An Attribute Value Directly

'''
class Car():
    """ A Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
'''

# Modifying AN Atrribute's Value Thorugh A Method

'''
class Car():
    """ A Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
'''
'''
class Car():
    """ A Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back on odometer")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2)
my_new_car.read_odometer()
'''

# Increementing An Attribute's Value Through A Method
'''
class Car():
    """ A Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back on odometer")

    def increement_odometer(self, miles):
        self.odometer_reading +=miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2)

my_new_car.increement_odometer(100)
my_new_car.read_odometer()
'''

# Inheritance

'''
class Car():  # parent class with all methods and attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + '' + self.model
        return long_name

    def read_odometer(self):
        print("Tis car has " + self.odometer_reading + " miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cannot roll back")

    def increement_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):  # child class in which 'parent class' defined in "()"
    """ Represent aspects of a car, specific to electric vehicles """

    def __init__(self, make, model, year):  # create an _init_ methods and pass the argument
        super().__init__(make, model, year)  # "super" class is call to create a connection b/w parent and child class


myTesla = ElectricCar('tesla ', ' model ', 2016)  # pass the parameters
print(myTesla.get_descriptive_name())  # print the 'values'
'''

# Defining An Attributes And Methods For the Child Class

'''
class Car():  # parent class with all methods and attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + '' + self.model
        return long_name

    def read_odometer(self):
        print("Tis car has " + self.odometer_reading + " miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cannot roll back")

    def increement_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):  # child class in which 'parent class' defined in "()"
    """ Represent aspects of a car, specific to electric vehicles """

    def __init__(self, make, model, year):  # create an _init_ methods and pass the argument
        super().__init__(make, model, year)  # "super" class is call to create a connection b/w parent and child class
        self.battery_size = 70  # define a new attribute

    def describe_battery(self): # create a new method
        print("This has a battery of size " + str(self.battery_size) + "kWh")


myTesla = ElectricCar('tesla ', ' model ', 2016)  # pass the parameters
print(myTesla.get_descriptive_name())  # print the 'values'
myTesla.describe_battery()   # call the new method

'''

# Overriding Methods from the Parent class

'''
class Car():  # parent class with all methods and attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 'CNG'  # declare an attribute for gas_tank

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + '' + self.model
        return long_name

    def fill_gas_tank(self, gas_tank):  # make a gas_tank method in main class
        print("This car need " + self.gas_tank + "gas tank!")

    def read_odometer(self):
        print("Tis car has " + self.odometer_reading + " miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cannot roll back")

    def increement_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):  # child class in which 'parent class' defined in "()"
    """ Represent aspects of a car, specific to electric vehicles """

    def __init__(self, make, model, year):  # create an _init_ methods and pass the argument
        super().__init__(make, model, year)  # "super" class is call to create a connection b/w parent and child class
        self.battery_size = 70

    def describe_battery(self):  # create a new method
        print("This has a battery of size " + str(self.battery_size) + "kWh")

    def ElectricCar(Car):
        
        def fill_gas_tank():
            print("This car does not need a gas tank!")


myTesla = ElectricCar('tesla ', ' model ', 2016)  # pass the parameters
print(myTesla.get_descriptive_name())  # print the 'values'
myTesla.describe_battery()  # call the new method
myTesla.ElectricCar()
'''

# Instance As An Attribute
# Example # 1
'''

class Car():  # parent class with all methods and attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + '' + self.model
        return long_name

    def read_odometer(self):
        print("Tis car has " + self.odometer_reading + " miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cannot roll back")

    def increement_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def  __init__(self , battery_size = 70):
        self.battery_size = battery_size


    def describe_battery(self):
        print("This car has a " +str(self.battery_size) + "-KWH battery")

class ElectricCar(Car):  # child class in which 'parent class' defined in "()"
    """ Represent aspects of a car, specific to electric vehicles """

    def __init__(self, make, model, year):  # create an _init_ methods and pass the argument
        super().__init__(make, model, year)  # "super" class is call to create a connection b/w parent and child class
        self.battery = Battery()  # define a new attribute and assign it to class "Battery"

myTesla = ElectricCar('tesla' , 'model' ,2016)
print(myTesla.get_descriptive_name())
myTesla.battery.describe_battery()
'''

'''

# Example # 2

class Car():  # parent class with all methods and attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + '' + self.model
        return long_name

    def read_odometer(self):
        print("Tis car has " + self.odometer_reading + " miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You cannot roll back")

    def increement_odometer(self, miles):
        self.odometer_reading += miles


class Battery():                                            # create a new class which is not inherited
    def __init__(self, battery_size=70):                    # define attributes
        self.battery_size = battery_size

    def describe_battery(self):                             # create a method for "describe_battery"
        print("This car has a " + str(self.battery_size) + "-KWH battery")

    def get_range(self):                                     # define a range fubc and perform 'if else' using range attribute
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):
    def __init__(self, make , model ,year):
        super().__init__(make,model,year)
        self.battery = Battery()        # assign 'self.battery' to class "Battery"

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery")


myTesla = ElectricCar('tesla', 'model', 2016)
print(myTesla.get_descriptive_name())
myTesla.battery.describe_battery()
myTesla.battery.get_range()                             # call class 'Battery' by assigning it 'battery' above and then call func 'range'

'''


'''
""" File copied from 9.4 to complete task of 9.10 """
class Restaurent():                                                                 # create a class(Restaurent)
    def __init__(self, rest_name,
                 cuisine_type):                                                     # create a func(_init_) and passes the parameters(self compulsary,name and cuisine type)
        self.rest_name = rest_name                                                  # assigning each parameter to a new var(rest_name)
        self.cuisine_type = cuisine_type                                            # assigning each parameter to a new var(cuisine_type)
        self.init_number_served = 0
        self.new_num_served=3
        self.num_served = 3
        self.update=0


    def describe_restaurent(self):                                                  # method to call each instance
        Restaurent = "Restaurent name is " + self.rest_name.title() + "Cuisine type of this retaurent is " + self.cuisine_type.title()
        return Restaurent

    def init_num_served(self):                                                       # give the initialliay number of people served i.e '0'
        print("Initially, this Restaurent served " + str(self.init_number_served))

    def new_number_served(self,new_num_served):                                      # give the initial number of people served i.e '3' passes in the parameter
        print("Now, restaurent has served " + str(self.new_num_served) + " customer")

    def update_num_served(self, update):                                             # give the more served of customer served i.e '4' must be greater than initial number of  people served otherwise it will be false
        if update >= self.new_num_served:
            self.update = update
            print("The restaurent has served " + str(self.update) + " more customer")

        else:
            print("You cannot add more served customer")

    def increement_num_served(self, served):                                          # give the increement number and total no. of customer served
        self.num_served += served + self.update
        print("The total number of customer served are: " + str(self.num_served))

    def rest_open(self):  # method to call 'message'                                  # method to print the greeting
        print(self.rest_name.upper() + " is opening!")
'''


'''

"""Copied from 9.8 to complete task of 9.11 and 9.12 """

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
        return long_name  # returning the name of a user

    def greet_users(self):
        print("Greetings " + self.f_name.title() + " " + self.l_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_attempts(self):
        self.login_attempts = 0


'''

'''
# The Python Standard Library
from collections import OrderedDict # begin with 'OrderedDict' class from importing it to module 'collections'
favorite_languages = OrderedDict() # create an instance of 'OrderedDict()'

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")
'''