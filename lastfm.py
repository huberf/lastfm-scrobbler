# Last.fm Syncing Tool
# Lean, fast, and functional
import os
import requests
import md5

api_head = 'http://ws.audioscrobbler.com/2.0/'
secret = 'the_secret_sauce'

def authorize(user_token):
    params = {
            'api_key': os.environ['LAST_FM_API'],
            'method': 'auth.getSession',
            'token': user_token
            }
    requestHash = hashRequest(params, secret)
    params['api_sig'] = requestHash
    apiResp = requests.post(api_head, params)
    return apiResp.text

def scrobble(song_name, artist_name, session_key):
    params = {
            'method': 'track.updateNowPlaying',
            'apiKey': os.environ['LAST_FM_API'],
            'track': song_name,
            'artist': artist_name,
            'sk': session_key
            }
    requestHash = hashRequest(params, secret)
    params['api_sig'] = requestHash
    apiResp = requests.post(api_head, params)
    return apiResp.text

def hashRequest(obj, secretKey):
    string = ''
    for i in obj.keys():
        string += i
        string += obj[i]
    string += secretKey
    stringToHash = string.encode('utf8')
    requestHash = md5.new(stringToHash).hexdigest()
    return requestHash
