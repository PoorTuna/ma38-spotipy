from Spotipy.core.music.spotipy_search import SpotipySearch
from Spotipy.core.music.spotipy_song_manager import SpotipySongManager
from Spotipy.core.users.spotipy_users.spotipy_user_manager import SpotipyUserManager
from Spotipy.core.users.user_manager import UserManager
from Spotipy.config.constants import ManagerConstants
from loguru import logger


class Spotipy:
    def __init__(self, user_manager: UserManager = None, song_manager: SpotipySongManager = None,
                 search_engine: SpotipySearch = None):
        self.user_manager = user_manager if user_manager is not None else SpotipyUserManager()
        self.song_manager = song_manager if song_manager is not None else SpotipySongManager()
        self.search_engine = search_engine if search_engine is not None else SpotipySearch(self.song_manager)

        logger.add(ManagerConstants.logs_path, rotation="12:00")
