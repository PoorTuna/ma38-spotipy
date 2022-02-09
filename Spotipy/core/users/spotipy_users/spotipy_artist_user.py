from typing import Dict

from Spotipy.core.users.spotipy_users.spotipy_premium_user import SpotipyPremiumUser


class SpotipyArtistUser(SpotipyPremiumUser):
    def __init__(self, name: str, password: str, albums: Dict[str, list] = {}):
        super().__init__(name, password)
        self.albums = albums
