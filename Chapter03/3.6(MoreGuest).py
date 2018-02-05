guestlst=['Ahmed', 'Ali', 'Hassan', 'Umar']
print("Now, new members are also invited for Bigger Table")

guestlst.insert(0,"Muhammad")
guestlst.insert(3,"Zubair")
guestlst.append(("Sameer"))

print("Guest 1(New): " +guestlst[0] + "\n" + "Guest 2: " +guestlst[1] + "\n" + "Guest 3: " +guestlst[2] + "\n" + "Guest 4(New): " +guestlst[3] + "\n" + "Guest 5: " + guestlst[4] + "\n" + "Guest 6: " + guestlst[5] + "\n" + "Guest 7(New):" + guestlst[6])
