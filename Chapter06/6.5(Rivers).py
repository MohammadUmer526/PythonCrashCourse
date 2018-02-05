Rivers={'Nile':'Egypt','jhelum':'Pakistan','bombaylake':'India'}

'''
#a)
for key, value in Rivers.items():
    print("The " + key.title() + " runs through a " + value)
'''

'''
#b)
for key,value in Rivers.items():        #both key var and value var must be use
    print("The rivers are: "+key)       #we just cal key var for only "Rivers"
'''


#c)

for riv_nam,country_name in Rivers.items():
    print("The name of countries is "+country_name)