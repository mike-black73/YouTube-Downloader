import re
from pytube import Playlist
from pytube import YouTube

print('put the video/playlist url here:')
link = input()
if 'Playlist' in link:
    playlist = Playlist(link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for url in playlist.video_urls:
       print(url)
       YouTube(url).streams.first().download()
elif 'watch' in link:
    YouTube(link).streams.first().download()
