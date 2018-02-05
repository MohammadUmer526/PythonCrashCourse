tour = {}

polling =True

while polling:
    person_name = input("What is your name: ")
    desried_place = input("Where do you want to go: ")

    tour[person_name] = desried_place

    more_place = input("Do you want to add more place(yes/no) ")
    if more_place =='no':
        polling =False

    for key , value in tour.items():
        print("Person "+key+ " want to go "+value+ " for tour")