import bcrypt


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password)
