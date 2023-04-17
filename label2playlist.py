import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import spotipy.util as util

playlist_uri = "https://open.spotify.com/user/wsd8gh9g3bwk64jl1oz3z1iul/playlist/3PB3H8NWnzR1ifZeap78dC?si=Iz48WtI6RASLxWhAA14dvA" # URI of playlist to add tracks to
label_name = "Clergy"

scope = "playlist-read-private playlist-modify-private playlist-modify-public"
token = util.prompt_for_user_token("wsd8gh9g3bwk64jl1oz3z1iul", scope, client_id='952433cc2fe94c069626be1bf33cddea',client_secret='2519a53239ca4c339728a611c8e7059d', redirect_uri='http://localhost:8080/')

sp = spotipy.Spotify(auth=token)
uri_list = []
list_of_100_uri_lists = []
offset = 0
prev_len = 0
while True:
	# pprint(sp.album("spotify:album:3LLA8KoCtMXJWBFQ51VckY"));exit()
	# pprint(sp.search('label:"Audiocode records"', type="album", limit=50))
	for album in sp.search(f'label:"{label_name}"', type="album", limit=50, offset=offset)["albums"]["items"]:
		# pprint(sp.album_tracks(album["id"]));exit()
		# pprint(sp.search(f'label:"{label_name}"', type="album", limit=50, offset=offset));exit()
		label_name_on_album = sp.album(album["id"])["copyrights"][0]["text"]
		# label_name_on_album = sp.album(album["id"])["copyrights"][0]["text"][5:] # for when there's a year in front of the label name
		# print(label_name_on_album[label_name_on_album.find(label_name):label_name_on_album.find(label_name) + len(label_name)]);exit()
		label_name_on_album = label_name_on_album[label_name_on_album.find(label_name):label_name_on_album.find(label_name) + len(label_name)]
		pprint(label_name_on_album)
		if label_name_on_album != label_name:
			break
		# pprint(album["artists"][0]["name"] + " - " + album["name"])
		# pprint(sp.album_tracks(album["id"]))
		for track in sp.album_tracks(album["id"])["items"]:
			# pprint(track["uri"])
			uri_list.append(track["uri"])
	

	# print(len(uri_list))
	
	# print("prev len:",prev_len)
	if prev_len == len(uri_list):
		break
	offset += 50
	prev_len = len(uri_list)

pprint(len(uri_list))
	
for i in range(0, len(uri_list), 100):
    x = i
    # pprint(uri_list[x:x+100])
    list_of_100_uri_lists.append(uri_list[x:x+100])

# pprint(list_of_100_uri_lists)

#index all track uris for all the retrieved albums
#put them all into arrays of max 100 size
#add 100 at a time to playlist


for lst in list_of_100_uri_lists:
	sp.playlist_add_items(playlist_uri, lst, position=None)