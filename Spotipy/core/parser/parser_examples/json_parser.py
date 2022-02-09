import os
from json import load

from Spotipy.core.exceptions.spotipy_parsers_exceptions import SpotipyJsonParserFileNotExistException


class JsonParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(path: str):
        if os.path.exists(path):
            with open(path, "r") as file_fd:
                return load(file_fd)
        raise SpotipyJsonParserFileNotExistException
