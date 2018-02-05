cities = {'karachi' : {'country' : 'pakistan' , 'population' : '17 crores' , 'fact' : 'islamic country'}, 'mumbai' : {'country' : 'india' , 'populatuion' : '115 crores' , 'fact' : '2 largest country by population'} , 'sydney' : {'country' : 'australia' , 'population' : '50 crores' , 'fact' : '9,000 beaches approx.'} , }

#create a dictionary which contains dictionary

for k , v in cities.items():                                                       #loop for dict
    print("Name of the city is " +k.title())                                       #printing name of city i.e key of "dict(cities)"
    print("belongs from " + v['country'].title() + " its fact is " + v['fact'])    #printing the value which is another dict(consist of key + value). So in tis casewe give 'key' of internal dict to get 'value' of that key i.e "coutry and fact"

