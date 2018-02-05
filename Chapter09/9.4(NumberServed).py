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


rest_1 = Restaurent('bbq tonight', 'bbq')  # create an instance
print(rest_1.describe_restaurent())  # call the method 1
rest_1.init_num_served()
rest_1.new_number_served(3)
rest_1.update_num_served(4)
rest_1.increement_num_served(33)
rest_1.rest_open()
