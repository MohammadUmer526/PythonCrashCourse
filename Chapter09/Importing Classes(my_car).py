""" To Run these program we must uncommented car.py in previous file i.e 'Classes' """
'''
# importing a  single class
from Classes import Car     # from 'class name' import 'particular class'
my_new_Car = Car('Audi' , 'a4', 2016)            # create an instance and passes the 'parameters'
print(my_new_Car.get_descriptive_name())

my_new_Car.odometer_reading = 23
my_new_Car.read_odometer()
'''

#Storing Multiple Classes in a Module
'''
from Classes import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

'''

'''
# Importing Multiple Classes
from Classes import ElectricCar, Car

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
'''

'''
# Importing an Entire Module

import Classes
my_beetle = Classes.Car('volkswagon','beetle' , 2016) # new instance = File_name.particularclass(parameter_1, parameter_2,...))
print(my_beetle.get_descriptive_name())

'''

'''
# Importing All Classes
from Classes import *

'''

'''

# Import A Module into Module

from Classes import Car
from my_electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

'''
