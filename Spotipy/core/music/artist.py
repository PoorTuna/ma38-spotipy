from typing import List

from Spotipy.core.music.album import Album


class Artist:
    def __init__(self, albums: List[Album] = []):
        self.albums = albums
