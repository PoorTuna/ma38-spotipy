from loguru import logger

from Spotipy.core.exceptions.spotipy_music_exceptions import SpotipyMusicPlaylistNameExistsException
from Spotipy.core.users.spotipy_users.spotipy_user import SpotipyUser


class SpotipyPremiumUser(SpotipyUser):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            logger.error(f"Playlist already exists with the name : {playlist_name} !")
            raise SpotipyMusicPlaylistNameExistsException

        self.playlists[playlist_name] = []
