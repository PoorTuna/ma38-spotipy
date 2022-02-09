from typing import List

from Spotipy.core.music.song import Song


class Album:
    def __init__(self, album_id: str, name: str, songs: List[Song] = []):
        self.songs = songs
        self.album_id = album_id
        self.name = name
