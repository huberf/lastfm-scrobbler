import extras
import datetime
import json

USER_NAME = 'your_user_name'
data = extras.user_daily_tracks(USER_NAME)
count = data['recenttracks']['@attr']['total']
print data['recenttracks']['track'][0]
print "Total Daily Tracks: " + str(count)

# 9*60*60
workday = 32400
dayStart = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%s")
currentTotal = float(datetime.datetime.today().strftime("%s")) - (float(dayStart) + (8*60*60))
ratio = workday/currentTotal
print "Expected scrobbles: " + str(int(int(count) * ratio))

data = extras.user_yearly_tracks(USER_NAME)
count = data['recenttracks']['@attr']['total']
print "Year Total: " + str(count)
yearStart = datetime.datetime(2018,1,1,0,0,0)
# Round up the day
current = datetime.datetime.now() + datetime.timedelta(days=1)
daysPassed = (current-yearStart).days
# Add your own yearly scrobble goal
yearGoal = 18000
requirement = (yearGoal/365)*daysPassed
print "Year Goal: " + str(requirement)
if count < requirement:
    print "You are behind. Try listening more to catch back up."
