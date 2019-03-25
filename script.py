import sys
import requests
import json


# The limit of albums returned from iTunes
LIMIT = 10

# Get the search term from the user if not in arguments
if len(sys.argv) == 1:
  term = raw_input("Enter search term: ").replace(" ", "+")
else:
  term = "+".join(sys.argv[1:])

geturl = "https://itunes.apple.com/search?entity=album&limit=%i&term=%s" % (LIMIT, term)
puturl = "http://restapis.tk/api/v1/albums"
auth = ("admin", "YouShallNotPass")

# Get some albums from the iTunes API
response = requests.get(geturl)
if response.status_code == 200:
  albums = response.json()['results']

# Slurp up some data from them and post it to restapis.tk
for album in albums:
  album_name = album['collectionName']
  album_artist = album['artistName']
  data = { 'name': album_name, 'artist': album_artist }
  r = requests.post(puturl, json=data, auth=auth)
  print u"Adding %s - %s: %i - %s" % (album_artist, album_name, r.status_code, r.reason)
