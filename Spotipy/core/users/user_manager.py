from collections import namedtuple


class UserManager:
    def __init__(self):
        self.users = {}  # {username : UserObj}

    class CurrentUser:
        curr_user = None
        is_authenticated = False
