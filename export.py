import extras
import json

upper = 99

allSongs = []

for i in range(1, upper + 1):
    print("Loading page " , i , " of " , upper)
    allSongs += extras.user_tracks('nhuberfeely', i)['recenttracks']['track']

print(len(allSongs))
jsonOut = json.dumps(allSongs);
f = open('archive.json', 'w')
f.write(jsonOut)
