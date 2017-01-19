# Last.fm Python Scrobbler

This is a lightweight script that can easily integrate with other applications
to provide scrobbling capabilities for any service.

*Warning:* This is a work in progress and not all functionality has been
finished or will function as intended.

## Setup
* First `git clone https://github.com/huberf/lastfm-scrobbler`
* Make sure you have the `requests` library installed.
* Create the environment variable `LAST_FM_API` with your [Last.fm API
  Key](http://www.last.fm/api/authentication)
* Now everything is ready and you simply have to include this file in your
  program and call the `authorize` or `scrobble` functions.


## Get user auth token
* Go to http://www.last.fm/api/auth?api_key={YOUR_API_KEY}&cb=http://localhost:5555
* Make sure nothing is running at port 5555, as we will be manually retreiving
  the token.
* Click "Allow Access"
* Now copy the token from the resulting url (e.g.
  `http://localhost:5555/?token={TOKEN_YOU_WANT}`)
* Now run the `authorize` function in this library with this token as the
  parameter.
* Profit?

## Scrobbling
* Import 'lastfm' into any project you want, and run the 'scrobble' function
  supplying the song name, artist name, and user auth token. The library will
  handle the rest. **Note:** This functionality does not fully function at this
  time.
