# Last.fm Python Scrobbler

This is a lightweight script that can easily integrate with other applications
to provide scrobbling capabilities for any service.

*Warning:* This is a work in progress and not all functionality has been
finished or will function as intended.

## Setup
* First `git clone https://github.com/huberf/lastfm-scrobbler'
* Make sure you have the `requests` library installed.
* Create the environment variable `LAST_FM_API` with your [Last.fm API
  Key](http://www.last.fm/api/authentication)
* Now everything is ready and you simply have to include this file in your
  program and call the `authorize` or `scrobble` functions.
