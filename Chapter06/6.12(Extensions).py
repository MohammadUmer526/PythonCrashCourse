favorite_languages = {'jen' : ['python' , 'java'], 'sara' : ['c'], 'edward' : ['ruby','go'], 'phil' : ['python','haskell'] , 'umer' : ['python' , 'java'] , 'ali' : ['C' , 'Cobol']}   #dict in which value is key

#add more key and values(another dictionary) in example of list in a dict and in dict in dict

'''

for k, v in favorite_languages.items():
    print(k.title()+ "'s " + " favorute languages are: ")
    for iv in v:
  print(""+iv.title())

'''


'''
#List in dict

for t , d in favorite_languages.items():                                                        #loop in which key, value of above dict are stored using items()
    print(t.title()+ "'s favorite languages are: ")                                             #printing keys in dict
    for e in d:                                                                                 #inner loop for printing value of each key
        print(e.title())

'''


#Dict in a dict

cities = {'karachi' : {'country' : 'pakistan' , 'population' : '17 crores' , 'fact' : 'its an islamic country'}, 'mumbai' : {'country' : 'india' , 'population' : '115 crores' , 'fact' : '2 largest country by population'} , 'sydney' : {'country' : 'australia' , 'population' : '50 crores' , 'fact' : '9,000 beaches approx.'} , 'washington' : {'country' : 'USA' , 'population' : '323 million' , 'fact' : 'Number 1 agency' } ,
'istanbul' : {'country' : 'turkey' , 'population' : '79 million' , 'fact' : 'Lies between Asia and Europe'} ,}


for k , v in cities.items():
    print("Name of city is "+k.title()+ "which is  belongs from "+v['country'].title() + ", its population is " + v['population'].title() + " and an interesting fact about this coubtry is " +v['fact'].title()+"\n")
