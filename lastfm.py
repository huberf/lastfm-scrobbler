# Last.fm Syncing Tool
import os
import requests

api_head = 'http://ws.audioscrobbler.com/2.0/'

def authorize(user_token):
    requestHash = None # TODO: Generate MD5 hash
    apiResp = requests.post(api_head, {'method': 'auth.getSession', 'apiKey': os.environ['LAST_FM_API'], 'apiSig': requestHash})
    return apiResp.text

def scrobble(song_name, artist_name):
    apiResp = requests.post('http://ws.audioscrobbler.com/2.0/', {'method': 'track.updateNowPlaying', 'apiKey': os.environ['LAST_FM_API'], 'track': song_name, 'artist': artist_name})
    print apiResp.text
