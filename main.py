import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from SpotifyClientCredentials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from listener import ObjectHoldingTheValue

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

#results = spotify.user
#print(results)

scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,scope=scope))

# results = sp.current_user()
# print(results)
result = sp.current_user_playing_track()
# result['item']['album']['name'] in case we need to know the album name
print(result['item']['name'])
for artist in result['item']['artists']:
    print(artist['name'])

result = sp.currently_playing()
playlist = result['context']['uri']

playlistInfo = spotify.playlist(playlist)
print(playlistInfo['name'])
# sp= spotify.client.Spotify(aut)

def print_if_different_song(old_value, new_value):
    if(old_value != new_value):
        print(f'The last song was: {old_value}, the new song is: {new_value}')

def print_if_different_playlist(old_value, new_value):
    if(old_value != new_value):
        print(f'The last playlist was: {old_value}, the new playlist is: {new_value}')

holder = ObjectHoldingTheValue()
holder.register_callback(print_if_different_song)

holder_playlist = ObjectHoldingTheValue()
holder_playlist.register_callback(print_if_different_playlist)

while(True):
    result = sp.current_user_playing_track()
    holder.value = result['item']['name']
    playlist = result['context']['uri']
    playlistInfo = spotify.playlist(playlist)
    holder_playlist.value = playlistInfo['name']
