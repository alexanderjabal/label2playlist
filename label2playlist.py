#!/usr/bin/python3

# TODO: add option to specify "released before the year x" for filtering albums for oldschool labels
# TODO: cleanup after adding to playlist: delete duplicates
# TODO: info banner at the top of the help page

import json
import argparse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint



def main(name):
	# auth_manager = SpotifyClientCredentials()
	# sp = spotipy.Spotify(auth_manager=auth_manager)
	scope = "playlist-read-private playlist-modify playlist-modify-private playlist-modify-public user-read-private user-read-email"
	
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
	label_name = name
	album_uris = []
	offset = 0
	
	print(f"[+] Gathering search results for label {label_name}")
	
	while True:
		results = sp.search(q=f'label:"{label_name}"', type="album", limit=50 , offset=offset)
		for album in results["albums"]["items"]:
			if sp.album(album["uri"])["label"] != label_name:
				continue
			album_uris.append(album["uri"])
	
		if len(results["albums"]["items"]) == 50:
			offset += 50
			continue
		else:
			break
	print(f"[!] Found {len(album_uris)} albums for label {label_name}")
	
	print(f"[+] Creating playlist for {label_name}")
	playlist = sp.user_playlist_create(user="wsd8gh9g3bwk64jl1oz3z1iul", name=label_name, public=False)
	
	print(f"[+] Adding tracks to playlist")
	
	track_uris_total = []

	for uri in album_uris:
		track_uris = []
		for track in sp.album_tracks(album_id=uri)["items"]:
			track_uris.append(track["uri"])
		# pprint(track_uris)
		sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
		track_uris_total.extend(track_uris)
	# pprint(track_uris_total)
	print(f"[+] Done!")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument( '-n', "--name", help="The name of the label", type=str, required=True, metavar="<label>")
	# parser.add_argument( '-rb', "--released-before", help="Only adds tracks from releases from before a certain year", type=int, required=False, metavar="<year>")
	args = parser.parse_args()

	main(args.name)
