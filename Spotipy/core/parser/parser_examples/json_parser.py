import os

from Spotipy.core.parser.parser import Parser
from json import load


class JsonParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(path):
        if os.path.exists(path):
            with open(path, "r") as file_fd:
                return load(file_fd)
        raise FileNotFoundError
