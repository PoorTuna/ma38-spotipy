import os
from json import load

from loguru import logger

from Spotipy.core.exceptions.spotipy_parsers_exceptions import SpotipyJsonParserFileNotExistException


class JsonParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(path: str):
        logger.debug("Checking json parser path validity...")
        if os.path.exists(path):
            with open(path, "r") as file_fd:
                logger.success("Successfully opened a json file!")
                return load(file_fd)
        logger.error("path does not exist!")
        raise SpotipyJsonParserFileNotExistException
