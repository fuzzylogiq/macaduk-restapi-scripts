term=$@
term=$(echo $term | sed 's/ /+/g')
albums=$(curl --silent --url "https://itunes.apple.com/search?term=$term&entity=album&limit=10")

echo $albums | python -c '
import sys
import json

albums = json.load(sys.stdin)["results"]

for album in albums:
  print album["collectionName"]
'


