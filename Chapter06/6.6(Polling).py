favorite_languages={'jen':'puthon',
                    'sarah':'c',
                    'edward':'ruby',
                    'phil':'python',}
people_list=['usama','sarah','ali','zaid','saad']                   #new list(polled members) where we check

for ask_pol in favorite_languages.keys():                           #loop for every element in dict and t will store in "ask_pol"

    if ask_pol in people_list:                                      #checking whether "fav_lang"(ask_pol) member registered or not?
        print(ask_pol.title()+" you already taken pol!")            #if yes then print"Already taken for poll"
    else:
        print(ask_pol.title()+" you are advised to take poll.")     #if not then print"to tell them for poll"