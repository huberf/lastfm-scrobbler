import lastpy.extras as extras
import datetime
import json

USER_NAME = 'nhuberfeely'
data = extras.user_daily_tracks(USER_NAME)
count = data['recenttracks']['@attr']['total']
noScrobbles = False
if len(data['recenttracks']['track']) == 0:
    noScrobbles = True
if not noScrobbles:
    lastTrack = data['recenttracks']['track'][0]
    print("Your last scrobble: " + str(lastTrack['name']) + ' by ' + str(lastTrack['artist']['#text']))
    print("Total Daily Tracks: " + str(count))
else:
    print("No scrobbles yet for today!")

# 9*60*60
workday = 32400
dayStart = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%s")
currentTotal = float(datetime.datetime.today().strftime("%s")) - (float(dayStart) + (8*60*60))
ratio = workday/currentTotal
if not noScrobbles:
    print("Expected scrobbles: " + str(int(int(count) * ratio)))
else:
    print("Start scrobbling to get your expected track count")

yesterday = extras.user_daily_tracks(USER_NAME, 1)
print("Yesterday scrobbles: " + str(yesterday['recenttracks']['@attr']['total']))

data = extras.user_yearly_tracks(USER_NAME)
count = int(data['recenttracks']['@attr']['total'])
print("Year Total: " + str(count))
yearStart = datetime.datetime(2018,1,1,0,0,0)
# Round up the day
current = datetime.datetime.now() + datetime.timedelta(days=1)
daysPassed = (current-yearStart).days
# Add your own yearly scrobble goal
yearGoal = 18000
requirement = int((yearGoal/365)*daysPassed)
print("Year Goal: " + str(requirement))
if count < requirement:
    print("You are behind. Try listening more to catch back up.")
