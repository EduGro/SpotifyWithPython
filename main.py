import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from SpotifyClientCredentials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from listener import ObjectHoldingTheValue
import time

# Log in
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)) 

# Reads the playback
scope = "user-read-playback-state"

# Log in for a registered user (so we can know the playback)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,scope=scope))


result = sp.current_user_playing_track()
# result['item']['album']['name'] in case we need to know the album name
print(result['item']['name']) # Prints song name
for artist in result['item']['artists']:
    print(artist['name'])

result = sp.currently_playing()
playlist = result['context']['uri']

playlistInfo = spotify.playlist(playlist)
print(playlistInfo['name'])

def print_if_different_song(old_value, new_value):
    if(old_value != new_value):
        print(f'The last song was: {old_value}, the new song is: {new_value}')

def print_if_different_playlist(old_value, new_value):
    if(old_value != new_value):
        print(f'The last playlist was: {old_value}, the new playlist is: {new_value}')

# Holder for listener in songs name
holder = ObjectHoldingTheValue()
holder.register_callback(print_if_different_song)

# Holder for listener in playlist change
holder_playlist = ObjectHoldingTheValue()
holder_playlist.register_callback(print_if_different_playlist)

while(True):
    result = sp.current_user_playing_track()
    holder.value = result['item']['name']
    playlist = result['context']['uri']
    playlistInfo = spotify.playlist(playlist)
    holder_playlist.value = playlistInfo['name']
    time.sleep(1)
