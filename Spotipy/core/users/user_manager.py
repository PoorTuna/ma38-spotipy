from Spotipy.core.users.spotipy_users.spotipy_user import SpotipyUser


class UserManager:
    def __init__(self):
        self.users = {}

    def signup(self, username: str, password: str):
        pass

    def login(self, username: str, password: str):
        pass

    def sign_out(self):
        self.CurrentUser.curr_user = None

    class CurrentUser:
        curr_user = None

        @staticmethod
        def is_authenticated(curr_user: SpotipyUser = curr_user):
            return curr_user if curr_user is not None else None
