from Spotipy.core.users.user import User


class SpotipyUser(User):
    def __init__(self, username: str, password: str):
        super(SpotipyUser, self).__init__(username, password)
        self.playlists = {}

    def add_playlist(self, playlist_name: str):
        pass
