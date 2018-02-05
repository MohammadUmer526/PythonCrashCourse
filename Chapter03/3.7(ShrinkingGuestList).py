print("You can invite only two people for dinner")
guestlst=['Muhammad','Ahmed', 'Ali', 'Hassan','Zubair','Umar']
print(guestlst)
msg1="Sorry " + guestlst[1] + ", we have no more space\n"
guestlst.pop(1)
print(msg1)
print(guestlst)

msg2="Sorry " + guestlst[2] +  " we have no more spce\n"
guestlst.pop(2)
print(msg2)
print(guestlst)

msg3="Sorry " + guestlst[1] + " we have no more space\n"
guestlst.pop(1)
print(msg3)
print(guestlst)

msg4=("Sorry " + guestlst[2] + " we have no more space\n")
guestlst.pop(2)
print(msg4)

print("Dear " + guestlst[0] + " and " + guestlst[1] + " you are still invited!")

del guestlst[0]
del guestlst[0]
guestlst.append("Haris")
del guestlst[0]
print(guestlst)