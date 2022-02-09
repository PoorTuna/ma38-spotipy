from Spotipy.core.users.spotipy_users.spotipy_user import SpotipyUser


class SpotipyFreeUser(SpotipyUser):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_playlist(self, playlist_name):
        if len(self.playlists) <= 5:
            pass  # raise an exception
        self.playlists[playlist_name] = []
