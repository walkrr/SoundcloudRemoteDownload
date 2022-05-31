## Soundcloud Remote Download with Metadata
Web app to download songs from youtube/soundcloud onto a remote server using youtube_dl, and allow easily setting the artist, song title and cover art. By default songs are automattically added to beets library on download. 
##Usage
Install the required modules, then run the webApp.py, browse to localhost:5000 and enter a link, after it is downloaded you will be redirected to a page with options to set metadata fields. Once you hit submit, the song from the requested link will be added with the selected metadata to your beets library.
## Use Cases
I personally listen to a lot of songs that aren't published on regular streaming services but can easily be found on soundcloud/youtube and use this to add them to my beets library with proper metadata that I then access from my phone through a subsonic server. 
## Future Features
#### Planned
- Add support for selecting local files from the server (and possibly client device) that don't have proper metadata
- Add support for uploading art from a local file
- Add support for embedding lyrics from a genuis link
- Add a tool for easily creating synced lyrics
- Setup an REST api
- Include more config options
- Add docker container
#### Possible?
- See if there is a way to easily sync with spotify local files(not sure how feasible this is)
