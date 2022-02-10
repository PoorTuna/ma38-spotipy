from typing import Dict

from loguru import logger

from Spotipy.core.exceptions.spotipy_music_exceptions import SpotipyInvalidSongFormatException
from Spotipy.core.music.album import Album
from Spotipy.core.music.artist import Artist
from Spotipy.core.music.song import Song


class SpotipySongManager:
    def __init__(self):
        self.albums = {}
        self.artists = {}
        self.songs = {}

    def add_song(self, dictionary: Dict[str, Dict]):
        """
        This function takes the dictionary formatted song and converts it into a series of objects.
        :param dictionary: the dictionary formatted song.
        :return: None
        """

        try:
            if dictionary["track"]["id"] not in self.songs:
                logger.debug("Adding a new song...")
                self.songs[dictionary["track"]["id"]] = Song(dictionary["track"]["id"], dictionary["track"]["name"],
                                                             dictionary["track"]["popularity"],
                                                             dictionary["track"]["album"]["id"])
                logger.success("Added a new song!")

            temp_song = self.songs[dictionary["track"]["id"]]

            self.__add_album(dictionary["track"]["album"], temp_song)

            for artist in dictionary["track"]["artists"]:
                self.__create_artist(artist, dictionary["track"]["album"]["id"], temp_song)

        except KeyError:
            logger.error("Got an invalid song format!")
            raise SpotipyInvalidSongFormatException

    def __add_album(self, album: Dict[str, str], song: Song):
        """
        This function creates a new album if not exists.
        :param album: The album dict to be added.
        :param song: The song object that needs to be added too if the album already exists.
        :return: None
        """
        if album["id"] in self.albums:
            self.__add_song(song, album)

        else:
            logger.debug("Adding a new album...")
            self.albums[album["id"]] = []
            self.albums[album["id"]].append([song])  # songs list
            self.albums[album["id"]].append(Album(*album.values()))
            logger.success("Added a new album!")

    def __create_artist(self, artist: Dict[str, str], album_id: str, song: Song):
        """
        This function gets an artist, a song and an album and initializes a new artist.
        :param artist: The artist dict
        :param album_id: Album id to be added
        :param song: Song object that adds the artist to itself.
        :return: None
        """
        if artist["id"] not in self.artists:
            self.artists[artist["id"]] = Artist(*artist.values())

        temp_artist = self.artists[artist["id"]]
        if album_id not in temp_artist.album_ids:
            temp_artist.album_ids.append(album_id)

        if temp_artist not in song.artists:
            song.artists.append(temp_artist)

    def __add_song(self, song: Song, album: Dict[str, str]):
        """
        This function gets a song and an album and adds the song to the album.
        :param song: The song object to be added.
        :param album: The album to be manipulated
        :return: None
        """
        logger.debug("Trying to add a new song with the album...")
        if song.name not in [song_name.name for song_name in self.albums[album["id"]][0]]:
            self.albums[album["id"]][0].append(song)
            logger.success("Added a new song!")
        else:
            logger.warning("Song already exists...")
