sandwich_orders = ['chicken' , 'pastrami' , 'club' , 'mayo', 'pastrami' , 'vegetable' , 'pastrami' ]
finished_sandwiches = []

print("Deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("")
while sandwich_orders:
    ordering_sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(ordering_sandwiches)
    print("You sandwiche "+ordering_sandwiches.title()+"is making...\n")

for finished_sandwiche in finished_sandwiches:
    print("New sandwiches are: "+finished_sandwiche)

