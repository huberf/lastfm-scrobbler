# Here are a few functions that aren't critical to properly scrobbling a song
# However, I they were fun to put together and might be of use to others.
import requests
import os

def user_tracks(user_name):
    resp = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=' + user_name + '&api_key=' + os.environ['LAST_FM_API'] + '&format=json')
    print resp.text
