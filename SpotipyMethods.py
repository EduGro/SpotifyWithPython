import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from SpotifyClientCredentials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from listener import ObjectHoldingTheValue
import time
import threading
from tkinter import Label, Tk, Button
import os


class SpotipyMethods:
    # Login
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
    # Reads the playback
    scope = "user-read-playback-state"
    # Log in for a registered user (so we can know the playback)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope))
    result = {}

    @classmethod
    def change_label_of_song_txt(cls, text):
        cls.write_in_file(text)

    @classmethod
    def get_current_song(cls):
        cls.result = cls.sp.current_user_playing_track()
        # result['item']['album']['name'] in case we need to know the album name
        if(cls.result != None):
            string = ""
            string += "Song name: " + cls.result['item']['name'] + '\n'  # song name
            string += "Artist(s): "
            artistList = []
            for artist in cls.result['item']['artists']:
                artistList.append(artist['name']) # All the artist here 
            string += ', '.join(artistList)
            string += '\n'
            albumURI = cls.result['item']['album']['uri'] # To know the label
            albumInfo = cls.sp.album(albumURI)
            string += "Label: " + albumInfo['label']
            return string
        else:
            return "Nothing is playing"

    @classmethod
    def print_if_different_song(cls, old_value, new_value):
        if(old_value['item']['name'] != new_value['item']['name']):
            return cls.get_current_song()

    @classmethod
    def get_current_song_listener(cls):
        print(cls.get_current_song())
        # Holder for listener in songs name
        holder = ObjectHoldingTheValue()
        holder.value = cls.result
        holder.register_callback(cls.print_if_different_song)

        while(True):
            cls.result = cls.sp.current_user_playing_track()
            holder.value = cls.result
            # Sleep (duration / 1000 -10(this is the crossfade))("duration_ms": 222075,)
            result = (cls.result['item']['duration_ms'] -cls.result['progress_ms'])/1000-6
            result_to_sleep = result if result > 0 else 1
            time.sleep(result_to_sleep)


    @classmethod
    def change_label_of_song(cls, label:Label):
        label.configure(text=cls.get_current_song())
        cls.change_label_of_song_txt(label.cget("text"))

        while(True):
            cls.result = cls.sp.current_user_playing_track()
            # Sleep (duration / 1000 -10(this is the crossfade))("duration_ms": 222075,)
            result = (cls.result['item']['duration_ms'] -cls.result['progress_ms'])/1000-6
            result_to_sleep = result if result > 0 else 1            
            time.sleep(result_to_sleep) 
            label.configure(text=cls.get_current_song())
            cls.change_label_of_song_txt(label.cget("text"))

    @classmethod
    def write_in_file(cls, text):
        direction = os.path.expanduser(r'~\Documents')

        f = open(direction, "w")
        f.write(text)
        f.close()

    