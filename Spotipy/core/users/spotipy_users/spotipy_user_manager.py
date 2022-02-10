import json
import os

from loguru import logger

from Spotipy.core.users.spotipy_users.spotipy_artist_user import SpotipyArtistUser
from Spotipy.core.users.spotipy_users.spotipy_free_user import SpotipyFreeUser
from Spotipy.core.users.spotipy_users.spotipy_premium_user import SpotipyPremiumUser
from Spotipy.core.users.user_manager import UserManager
from Spotipy.core.exceptions.spotipy_users_exceptions import SpotipyUsernameAlreadyExistsException
from Spotipy.config.constants import ManagerConstants


class SpotipyUserManager(UserManager):
    def __init__(self):
        super().__init__()
        # self.sync_user_db()

    def signup(self, username: str, password: str, premium: bool = False, artist: bool = True):
        super().signup(username, password)
        logger.debug(f"A registration attempt with {username}")

        if username in self.users:
            logger.warning(f"{username}, username already exists!")
            raise SpotipyUsernameAlreadyExistsException

        if not artist:
            self.users[username] = SpotipyPremiumUser(username, password) if premium else SpotipyFreeUser(username,
                                                                                                          password)
        else:
            self.users[username] = SpotipyArtistUser(username, password)

        if os.path.exists(ManagerConstants.user_db_path):
            with open(ManagerConstants.user_db_path, "a") as spotipy_fd:
                pass
        else:
            with open(ManagerConstants.user_db_path, "w") as spotipy_fd:
                pass

        logger.success(f"User: {username} successfully registered!")

    def login(self, username: str, password: str):
        logger.debug(f"Login attempt with {username}!")
        if username in self.users:
            if self.users[username].validate_password(password):
                self.current_user.curr_user = self.users[username]
                logger.success(f"User: {username} has successfully logged in!")

            else:
                logger.warning(f"A login attempt has been made with : {username} . Incorrect Password!")

        else:
            logger.error(f'User "{username}" does not exist!')

    def sync_user_db(self):
        if os.path.exists(ManagerConstants.user_db_path):
            with open(ManagerConstants.user_db_path, "r") as spotipy_fd:
                for user in spotipy_fd:
                    # print(self.users, user)
                    pass
        else:
            with open(ManagerConstants.user_db_path, "x"):
                pass


# xd = SpotipyUserManager()
# xd.signup("hello", "world")
