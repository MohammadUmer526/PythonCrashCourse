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

    def upgrade_battery(self):
        if self.battery_size == 70:
            capacity = 85

        elif self.battery_size == 85:
            capacity = 50

        message2 = "The car has a capacity of " + str(capacity)
        message2 += " miles on it"
        print(message2)
class ElectricCar(Car):
    def __init__(self, make , model ,year):
        super().__init__(make,model,year)
        self.battery = Battery()        # assign 'self.battery' to class "Battery"

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery")
myTesla = ElectricCar('tesla', 'model', 2016)
print(myTesla.get_descriptive_name())
myTesla.battery.describe_battery()
myTesla.battery.get_range()
myTesla.battery.upgrade_battery()