import bcrypt
from loguru import logger


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password):
        logger.debug(f"Login attempt as {self.username}. Checking password validity...")
        return bcrypt.checkpw(password.encode(), self.password)
