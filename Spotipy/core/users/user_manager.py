class UserManager:
    def __init__(self):
        self.users = {}

    class CurrentUser:
        curr_user = None
        is_authenticated = False
