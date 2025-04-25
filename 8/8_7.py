def make_album(artist, album):
	dict_album = {
		'artist': artist.title(),
		'album': album.title(),
	}
	return dict_album

album = make_album('metallica', 'dead magnetic')
print(album)

album = make_album('metaa', 'magnetic')
print(album)

album = make_album('metica', 'ead magnetic')
print(album)


# def make_album(artist, album, track=None):
# 	if track:
# 		dict_album = {
# 		'artist': artist.title(),
# 		'album': album.title(),
# 		'track': track,
# 		}
# 	else:
# 		dict_album = {
# 			'artist': artist.title(),
# 			'album': album.title(),
# 		}
# 	return dict_album


def make_album(artist, album, track=None):
	
	dict_album = {
	'artist': artist.title(),
	'album': album.title(),
		}
	
	if track:
		dict_album['track'] = track
	
album = make_album('metallica', 'dead magnetic')
print(album)

album = make_album('metaa', 'magnetic')
print(album)

album = make_album('metica', 'ead magnetic')
print(album)

album = make_album('metica', 'ead magnetic', 5)
print(album)