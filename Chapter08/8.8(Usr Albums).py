def make_user_album(artist_name_1 , album_name_1 , artist_name_2 , album_name_2 , artist_name_3 , album_name_3):
    dict_1 = {'First Artist Name': artist_name_1, 'First Album Name': album_name_1}

    dict_2 = {'Second Artist Name': artist_name_2, 'Second Album Name': album_name_2}

    dict_3 = {'Third Artist Name': artist_name_3, 'Third Album Name': album_name_3}

    dictionaries = "First Dictionary: " + str(dict_1) + " \n" "Second Dictionary:"  + str(dict_2)+ "\n"+ "Third Dictionary" + str(dict_3)

    return dictionaries

while True:

 artist_name_1=input("Enter your name: ")

 if artist_name_1=='q' or artist_name_1 == 'quit':
     break

 album_name_1 = input("Enter your album name: ")

 if album_name_1=='q' or album_name_1 == 'quit':
     break

 artist_name_2 = input("Enter your name: ")

 if artist_name_2=='q' or artist_name_2 == 'quit':
     break

 album_name_2 = input("Enter your album name: ")

 if album_name_2=='q' or album_name_2 == 'quit':
     break

 artist_name_3 = input("Enter your name: ")

 if artist_name_3=='q' or artist_name_3 == 'quit':
     break

 album_name_3 = input("Enter your album name: ")

 if album_name_3=='q' or album_name_1 == 'quit':
     break

 message = make_user_album(artist_name_1,album_name_1,artist_name_2,album_name_2,artist_name_3,album_name_3)
 print(message)