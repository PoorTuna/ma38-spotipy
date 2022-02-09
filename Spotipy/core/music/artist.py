from typing import List

from Spotipy.core.music.album import Album


class Artist:
    def __init__(self, id: str, name: str, albums: List[Album] = []):
        self.albums = albums
        self.id = id
        self.name = name
