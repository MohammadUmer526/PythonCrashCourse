from collections import OrderedDict  # import class 'OrderedDict' from module 'collections'
glossary = OrderedDict() # create an instance of 'OrderedDict'

glossary={'list':'contains set of elements & muteable.','tuple':'contains set of elements & immuteable.','remove':'delete item by value.','delete':'also delete item but permanently.','insert':'insert an element, takes two argument in first index of an item and second contain value.',}
for gloss_key, gloss_value in glossary.items():
    print("The term " + gloss_key + "'s meaning in Python is " + gloss_value.title() + ".")