import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from SpotifyClientCredentials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

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

result = spotify.playlist(playlist)
print(result['name'])
# sp= spotify.client.Spotify(aut)