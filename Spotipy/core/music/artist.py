from typing import List


class Artist:
    def __init__(self, artist_id: str, name: str, album_ids: List[str] = []):
        self.album_ids = album_ids
        self.artist_id = artist_id
        self.name = name
