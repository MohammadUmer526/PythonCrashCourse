# I copied Restaurent class from 9.4(file) and paste it into 'Classes' file
from Classes import Restaurent # it may give error, must uncommented class 'Restaurent' from 'Classes'
rest_1 = Restaurent('bbq tonight', 'bbq')  # create an instance
print(rest_1.describe_restaurent())  # call the method 1
rest_1.init_num_served()
rest_1.new_number_served(3)
rest_1.update_num_served(4)
rest_1.increement_num_served(33)
rest_1.rest_open()
