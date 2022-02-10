from Spotipy.core.users.spotipy_users.spotipy_user import SpotipyUser


class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = self.__CurrentUser()

    def signup(self, username: str, password: str):
        pass

    def login(self, username: str, password: str):
        pass

    def sign_out(self):
        self.current_user.curr_user = None

    class __CurrentUser:
        def __init__(self):
            self.curr_user = None

        def is_authenticated(self):
            return self.curr_user if self.curr_user is not None else None
