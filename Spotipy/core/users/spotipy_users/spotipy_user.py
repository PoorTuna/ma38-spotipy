from Spotipy.core.users.user import User


class SpotipyUser(User):
    def __init__(self, username, password):
        super(SpotipyUser, self).__init__(username, password)

    def add_playlist(self, playlist_name):
        pass
