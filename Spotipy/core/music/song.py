from typing import List


class Song:
    def __init__(self, song_id: int, name: str, popularity: int, album_id: str, artists: list = [],
                 genres: List[str] = []): # TODO : think of a clever way to import artist class without causing a circular import
        self.song_id = song_id
        self.name = name
        self.popularity = popularity
        self.album = album_id
        self.artists = artists
        self.genres = genres
