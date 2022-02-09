from Spotipy.core.music.spotipy_song_manager import SpotipySongManager
from Spotipy.core.users.spotipy_users.spotipy_user_manager import SpotipyUserManager
from Spotipy.core.users.user_manager import UserManager


class Spotipy:
    def __init__(self, user_manager: UserManager = None, song_manager: SpotipySongManager = None):
        self.user_manager = user_manager if not None else SpotipyUserManager()
        self.song_manager = song_manager if not None else SpotipySongManager()
