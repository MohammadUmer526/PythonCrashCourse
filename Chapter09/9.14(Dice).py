from random import randint    # import 'randint' from module 'random'
class Dice():

    x = randint(1, 6)
    def __init__(self , sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

d6 = Dice() # first instance of die

results = []  # create an empty list
for ab in range(10):
    rslt = d6.roll_die()
    results.append(rslt)
print("10 roll of a 6 sided are: ")
print(results)

d10 = Dice(sides = 10) # second instance of die

results = []

for xy in range(10):
    rslt2 = d10.roll_die()
    results.append(rslt2)
print("10 roll of a 10 sided are: ")
print(results)


d10 = Dice(sides = 20)  # third instance of die

results = []

for pq in range(10):
    rslt3 = d10.roll_die()
    results.append(rslt3)
print("10 roll of a 20 sided are: ")
print(results)
