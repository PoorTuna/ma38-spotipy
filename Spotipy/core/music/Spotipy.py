from typing import Dict

from Spotipy.core.music.album import Album
from Spotipy.core.music.artist import Artist
from Spotipy.core.music.song import Song


class Spotipy:
    def __init__(self):
        self.albums = {}  # {album_id : [ [songs], name], album_id2 : [ [songs], name]}

    def add_song(self, dictionary: Dict[str, str]):
        """
        This function takes the dictionary formatted song and converts it into a series of objects.
        :param dictionary: the dictionary formatted song.
        :return: None
        """
        temp_song = Song(dictionary["track"]["id"], dictionary["track"]["name"], dictionary["track"]["popularity"],
                         dictionary["track"]["album"]["id"])

        album_temp = Album(*dictionary["track"]["album"].values())

        for artist in dictionary["track"]["artists"]:
            artist_temp = Artist(*artist)
            album_temp.songs.append(temp_song)
            artist_temp.albums.append(album_temp)

            temp_song.artists.append(artist_temp)

        if album_temp.album_id in self.albums:
            self.albums[album_temp.album_id][0].append(temp_song)

        else:
            self.albums[album_temp.album_id] = []
            self.albums[album_temp.album_id].append([])  # songs list
            self.albums[album_temp.album_id].append(album_temp.name)
