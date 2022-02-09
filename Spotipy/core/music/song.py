from typing import List


class Song:
    def __init__(self, popularity: int = 0, genres: List[str] = []):
        self.popularity = popularity
        self.genres = genres
