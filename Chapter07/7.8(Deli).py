sandwich_ordes = ['chicken' , 'club' , 'mayo' ,'vegetable']
finished_sandwiches = []

while sandwich_ordes:
    ordering_sandwiches = sandwich_ordes.pop()
    finished_sandwiches.append(ordering_sandwiches)
    print("Adding "+ordering_sandwiches.title())

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche + " made sandwich for you.")
