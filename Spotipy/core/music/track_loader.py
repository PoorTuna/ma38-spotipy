from typing import Dict

from Spotipy.core.music.artist import Artist


class TrackLoader:
    def __init__(self):
        pass

    @staticmethod
    def loader(dictionary: Dict[str]):
        for artist in dictionary["track"]["artists"]:

            artist_temp = Artist(**artist)

            artist_temp.albums.append(**dictionary["track"]["album"])
