from typing import Dict

from Spotipy.core.music.album import Album
from Spotipy.core.music.artist import Artist
from Spotipy.core.music.song import Song


class TrackLoader:
    def __init__(self):
        pass

    @staticmethod
    def loader(dictionary: Dict[str, str]):
        """
        This function takes the dictionary formatted song and turns it into a series of objects
        :param dictionary:
        :return:
        """
        temp_song = Song(dictionary["track"]["id"], dictionary["track"]["name"], dictionary["track"]["popularity"],
                         dictionary["track"]["album"]["id"])

        for artist in dictionary["track"]["artists"]:
            artist_temp = Artist(**artist)
            album_temp = Album(**dictionary["track"]["album"])
            album_temp.songs.append(temp_song)
            artist_temp.albums.append(album_temp)

            temp_song.artists.append(artist_temp)
