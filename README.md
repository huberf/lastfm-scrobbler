# Last.fm Python Scrobbler

This is a lightweight script that can easily integrate with other applications
to provide scrobbling capabilities for any service.

## Setup (With Pip)
* Run `pip install lastpy`
* Create the environment variable `LAST_FM_API` and `LAST_FM_API_SECRET` with your [Last.fm API
  Key](http://www.last.fm/api/authentication)
* Now import the library, and run the `scrobble` function to start saving songs.

## Setup (From Source)
* First `git clone https://github.com/huberf/lastfm-scrobbler`
* Make sure you have the `requests` library installed.
* Create the environment variable `LAST_FM_API` and `LAST_FM_API_SECRET` with your [Last.fm API
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
* Import 'lastpy' into any project you want, and run the 'scrobble' function
  supplying the song name, artist name, and user auth token. The library will
  handle the rest.

## Extras
To view account data retreival, consult the `statusreport.py` file in this repo.
