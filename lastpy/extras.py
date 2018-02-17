# Here are a few functions that aren't critical to properly scrobbling a song
# However, I they were fun to put together and might be of use to others.
import requests
import json
import datetime
import os

api_root = 'http://ws.audioscrobbler.com/2.0/'

def user_tracks(user_name, page):
    resp = requests.get(api_root + '?method=user.getrecenttracks&user=' + user_name + '&api_key=' + os.environ['LAST_FM_API'] + '&page=' + str(page) + '&format=json')
    return json.loads(resp.text)

def user_weekly_tracks(user_name):
    resp = requests.get(api_root + '?method=user.getweeklytrackchart&user=' + user_name + '&api_key=' + os.environ['LAST_FM_API'] + '&format=json')
    return json.loads(resp.text)

def user_daily_tracks(user_name):
    dayStart = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%s")
    resp = requests.get(api_root + '?method=user.getrecenttracks&user=' + user_name + '&api_key=' + os.environ['LAST_FM_API'] + '&from=' + str(dayStart) + '&limit=200' +'&format=json')
    return json.loads(resp.text)

def user_yearly_tracks(user_name):
    dayStart = datetime.datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0).strftime("%s")
    resp = requests.get(api_root + '?method=user.getrecenttracks&user=' + user_name + '&api_key=' + os.environ['LAST_FM_API'] + '&from=' + str(dayStart) + '&limit=1000' +'&format=json&page=1')
    return json.loads(resp.text)
