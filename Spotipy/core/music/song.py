from typing import List


class Song:
    def __init__(self, song_id: int, name: str, popularity: int, album_id: str, artists_ids: list = [],
                 genres: List[str] = []):
        self.song_id = song_id
        self.name = name
        self.popularity = popularity
        self.album = album_id
        self.artists = artists_ids
        self.genres = genres
