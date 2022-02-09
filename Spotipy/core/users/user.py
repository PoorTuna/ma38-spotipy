import bcrypt


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())

    def validate_password(self, password):
        return bcrypt.checkpw(self.password, password)