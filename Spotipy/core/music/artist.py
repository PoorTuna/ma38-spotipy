from typing import List

from Spotipy.core.music.album import Album


class Artist:
    def __init__(self, artist_id: str, name: str, albums: List[Album] = []):
        self.albums = albums
        self.artist_id = artist_id
        self.name = name
