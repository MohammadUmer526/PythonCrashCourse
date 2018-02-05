def describe_city(city='karachi', country='pakistan'):
    print(city.title()+" is in the "+country.title())
describe_city()                                             #call deafult parameter
describe_city('lahore')                                     #add'Lahore' in city
describe_city('mumbai','india')                             #new City(mumbai) and new country(India)

#Note: All the arguments pass individually 1st, 2nd & 3rd.