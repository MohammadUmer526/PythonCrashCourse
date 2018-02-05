msg = "Enter the toppings: \nEnter quit for exit."

while msg!='quit':                                              #loop for condition

    message = input(msg)                                        #prompt input 'msg'
    print("You add: "+message.title() + "in the topping list\n")      #print