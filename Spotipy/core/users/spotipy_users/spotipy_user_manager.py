from loguru import logger

from Spotipy.core.users.spotipy_users.spotipy_free_user import SpotipyFreeUser
from Spotipy.core.users.spotipy_users.spotipy_premium_user import SpotipyPremiumUser
from Spotipy.core.users.user_manager import UserManager
from Spotipy.core.exceptions.spotipy_users_exceptions import SpotipyUsernameAlreadyExistsException


class SpotipyUserManager(UserManager):
    def __init__(self):
        super().__init__()

    def signup(self, username: str, password: str, premium: bool = False, artist: bool = True):
        super(SpotipyUserManager, self).signup(username, password)

        if username in self.users:
            logger.warning(f"{username} already exists!")
            raise SpotipyUsernameAlreadyExistsException

        self.users[username] = SpotipyPremiumUser(username, password) if premium else SpotipyFreeUser(username,
                                                                                                      password)

    def login(self, username: str, password: str):
        if username in self.users:
            if self.users[username].validate_password(password):
                logger.success(f"User: {username} has successfully logged in!")

            else:
                logger.warning(f"A login attempt has been made with : {username} . Incorrect Password!")


xd = SpotipyUserManager()

xd.signup("xd", "lmao")
