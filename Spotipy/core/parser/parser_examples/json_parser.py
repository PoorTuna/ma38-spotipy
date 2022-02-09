import os
from json import load


class JsonParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(path: str):
        if os.path.exists(path):
            with open(path, "r") as file_fd:
                return load(file_fd)
        raise FileNotFoundError
