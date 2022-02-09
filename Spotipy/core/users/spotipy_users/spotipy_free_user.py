from Spotipy.core.exceptions.spotipy_users_exceptions import SpotipyMusicPlaylistCountException, \
    SpotipyMusicPlaylistNameExistsException
from Spotipy.core.users.spotipy_users.spotipy_user import SpotipyUser
from Spotipy.config.constants import UserConstants


class SpotipyFreeUser(SpotipyUser):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_playlist(self, playlist_name):
        if len(self.playlists) <= UserConstants.free_user_playlist_limit:
            raise SpotipyMusicPlaylistCountException
        if playlist_name in self.playlists:
            raise SpotipyMusicPlaylistNameExistsException

        self.playlists[playlist_name] = []
