def make_album(artist, title):
	music_album = {'artist': artist.title(), 'title': title.title()}
	return music_album


while True:
	print("Enter an album's title and artist")
	print("Enter 'quit' anytime if you want to quit")
	title = input("Enter an album title: \n")
	if title.lower() == 'quit':
		break
	artist = input("Enter an album artist: \n")
	if artist.lower() == 'quit':
		break
	print(make_album(artist, title))
	another_person = input("Do you want to add another title and artist?(y/n)")
	if another_person.lower() == 'n':
		break

