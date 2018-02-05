class Restaurent():
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def decribe_rest(self):
        print("Restaurent name is " + self.rest_name.title())
        print("Cuisine type is " + self.cuisine_type.title()+"\n")

    def rest_open(self):
        print(self.rest_name.title() + " is opening!")


rest_1 = Restaurent('pear continental', 'sea food')
rest_2 = Restaurent('moven pick', 'fast food')
rest_3 = Restaurent('bbq tonight', 'bbq')

rest_1.decribe_rest()
rest_2.decribe_rest()
rest_3.decribe_rest()

rest_1.rest_open()
rest_2.rest_open()
rest_3.rest_open()
