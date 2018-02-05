def make_album(artist_name_1 , album_title_1, artist_name_2 , album_title_2 , artist_name_3, album_title_3):

    album_1 = {'artist_1' :  artist_name_1 , 'album_1 title' : album_title_1 }

    album_2 = {'artist_2' : artist_name_2 ,  'album_2 title' : album_title_2}

    album_3 = {'artist_2': artist_name_3, 'album_2 title': album_title_3}

    albums = str(album_1) + "\n" + str(album_2) + "\n" + str(album_3)
    return albums
message = make_album('john','sem','sean','seree','tommy','ovaaal')
print(message)