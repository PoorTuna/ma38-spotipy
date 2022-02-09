from typing import List


class Song:
    def __init__(self, id: int, name: str, popularity: int, genres: List[str] = []):
        self.popularity = popularity
        self.genres = genres

