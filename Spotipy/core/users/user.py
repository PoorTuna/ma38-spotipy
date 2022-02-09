import bcrypt
from abc import abstractmethod, ABC


class SpotipyUser(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.playlists = {}

    def validate_password(self, password):
        return bcrypt.checkpw(self.password, password)

    @abstractmethod
    def add_playlist(self, playlist_name):
        pass
