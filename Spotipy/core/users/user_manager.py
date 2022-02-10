class UserManager:
    def __init__(self):
        self.users = {}

    def signup(self, username, password):
        pass

    def login(self, username, password):
        pass

    class CurrentUser:
        curr_user = None
        is_authenticated = False
