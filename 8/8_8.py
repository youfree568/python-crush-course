def make_album(artist, album, tracks=None):
	dict_album = {
		'artist': artist.title(),
		'album': album.title(),
	}
	return dict_album

while True:
	print("Enter name of artist and album.\nIf you want to leave press 'q'")
	artist = input("Artist: ")
	if artist == 'q':
		break
	album = input("Album: ")

	if album == 'q':
		break
	
	print(make_album(artist, album))