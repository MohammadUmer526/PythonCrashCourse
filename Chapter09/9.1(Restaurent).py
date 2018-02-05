class Restaurent():                                                                #create a class(Restaurent)
    def __init__(self, rest_name , cuisine_type):                                  #create a func(_init_) and passes the parameters(self compulsary,name and cuisine type)
        self.rest_name = rest_name                                                 #assigning each parameter to a new var(rest_name)
        self.cuisine_type = cuisine_type                                           #assigning each parameter to a new var(cuisine_type)

    def describe_restaurent(self):                                                 #method to call each instance
        print("Restaurent name is " + self.rest_name.title())
        print("Cuisine type of this retaurent is " + self.cuisine_type.title())

    def rest_open(self):                                                           #method to call 'message'
        print(self.rest_name.upper() + " is opening!")

rest_1 = Restaurent('bbq tonight' , 'bbq')                                         #create an instance
rest_1.describe_restaurent()                                                       #call the method 1
rest_1.rest_open()                                                                 #call the method 2

