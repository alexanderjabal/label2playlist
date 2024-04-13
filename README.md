
# Label 2 Playlist

A script that allows the user to search for any record label and have a playlist containing all its releases (that are available on Spotify) be automatically generated and added to the user's library.

This project was born out of a combination of two of my biggest hobbies: DJ'ing and programming. Digging for tracks by label is an amazing way to discover new (and old!) music. But it proved quite tiresome to search for many label releases on YouTube or Discogs separately and listen to the tracks that way. If only there was a way to just type in a label's name and get (almost) all of its releases presented to you in a single, easy to sort through list. 

Well, now there is, kinda.

Simply run `python3 label2playlist.py -n <label>` and the script will use the Spotify API to perform an advanced search query for all albums that have the label tag set to the supplied name, parse all the results and add them all to a playlist. Easy as that.

This tool has already helped me massively in discovering new music, as I can just put on a playlist when I go out and listen to hundreds of new tracks, instead of having to constantly open YouTube to endure yet another bad sounding vinyl rip.

I'll work on this tool on and off in the future, I have some features that I want to add, but for now it works just fine.

## First time usage

If you run the script for the first time, you'll first be prompted to authenticate using your Spotify account. This authentication is completely server side and no credentials are stored by the script. After this is done you can continue to use the script as normal.

## Known issues

When the supplied label is old and tends to have many releases, there is a large chance that there will be a few duplicates in the playlist. I will be fixing this in the future.
