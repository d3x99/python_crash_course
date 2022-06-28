def make_album(artist, title, number_of_songs = None):
	music_album = {'artist': artist.title(), 'title': title.title()}
	if number_of_songs:
		music_album['number of songs'] = number_of_songs
	return music_album

album1 = make_album("Me", "Road to knowhere")
album2 = make_album("You", "Road to Anywhere", 12)
print(album1)
print(album2)