from Spotipy import spotipy
from Spotipy.core.parser.parser_examples import json_parser

from Spotipy.core.users.spotipy_users.spotipy_user_manager import SpotipyUserManager
from Spotipy.core.users.spotipy_users.spotipy_free_user import SpotipyFreeUser
from Spotipy.core.users.spotipy_users.spotipy_premium_user import SpotipyPremiumUser
from Spotipy.core.users.spotipy_users.spotipy_artist_user import SpotipyArtistUser

from Spotipy.core.music.spotipy_search import SpotipySearch
from Spotipy.core.music.spotipy_song_manager import SpotipySongManager

from Spotipy.core.exceptions import *

from Spotipy.config.constants import *


def spotipy_music_class():
    from Spotipy.core.music.song import Song
    from Spotipy.core.music.artist import Artist
    from Spotipy.core.music.album import Album


def user_class():
    from Spotipy.core.users.user import User
    from Spotipy.core.users.user_manager import UserManager
