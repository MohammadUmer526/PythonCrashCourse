#Importing an Entire Function
"""
import Function
Function.make_pizza(10 , "pepperoni")                     `#passing parameter i.e size and single topping
Function.make_pizza(12, "extra cheese", "mushrooms")

"""

#Importing a Specific Function
'''
from Function import make_pizza                             #from module_name import function name
make_pizza(23, 'pepperoni' , 'mushrooms')
'''

#Using As To Give A Function as Alice

'''
from Function import make_pizza as mp                       #give func(make_pizza) new name(alice) as 'mp'
mp(19,'pepperoni' , 'mushrooms')                            #pass the argument
'''


#Using As To Give A Module as Alice
'''

import Function as p                                        # import funct_name as new_name(alice) as 'p'
p(88,'pepperoni' , 'mushrooms')

'''

#Importing All Functions in a Module
'''
from Function import *                                      # from module_name import '*' for all function in a module
make_pizza(55,'pepperoni' , 'mushrooms')
'''