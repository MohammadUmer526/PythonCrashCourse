favfruits=['Grapes','Banana','Dates','Guava','Pineapple']
#if 'Apple' and 'Banana' and 'Mango' and 'Guava' and 'Pineapple' in favfruits:              #if we use and operator then it will execute true because only one element must be same.
#    print("Inserted elements are on the list!")
#else:
#    print("SOme elements are missing!")

favorite_fruit=['Grapes','Avacado','Dates']

if favfruits[0] in favorite_fruit:
    print("I really like",favfruits[0]+"\n")
else:
    print("Element not found!\n")

if favfruits[1] in favorite_fruit:
    print("I really like",favfruits[1])
else:
    print("Elements not found!\n")

if favfruits[2] in favorite_fruit:
    print("I really like",favfruits[2]+"\n")
else:
    print("Elements not found!\n")

if favfruits[3] in favorite_fruit:
    print("I really like",favfruits[3]+"\n")
else:
    print("Elements not found!\n")

if favfruits[4] in favorite_fruit:
    print("I really like ",favorite_fruit[4]+"\n")
else:
    print("Elements not found!\n")