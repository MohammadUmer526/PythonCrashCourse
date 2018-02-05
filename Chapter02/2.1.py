name="m. umer khan"
print(name.title()) #tile, every first letter of each word has Cap
print(name.lower()) # every letter is small
print(name.upper()) # every letter is Cap
''' 
Concatenation
'''
var1 = "Muhammad"
var2= "Umer"
full_name = var1 + " " + var2
print(full_name)

''' Concatenation with upper and lower case'''

print(full_name.lower())
''' White Space'''

print("languages: \npython\nJava")

''' White Space with tabs and new lines'''
print("Languages: \n\tPython\n\tjava\n\tjavaScript")
''' White Space Stripping'''
favorit_language=" Python   "
print(favorit_language)
print(favorit_language.lstrip())
print(favorit_language.rstrip())
print(favorit_language.strip())
''' Avoiding Syntex Error'''

mesage= ("One of the feature of python's is, its not use semicolon") # use "" to avoid the errors
print(mesage
      )