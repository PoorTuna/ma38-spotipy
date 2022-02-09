from typing import List

from Spotipy.core.music.song import Song


class Album:
    def __init__(self, songs: List[Song] = []):
        self.songs = songs
