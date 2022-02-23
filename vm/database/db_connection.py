import sqlite3

from vm.config import PATH_DATABASE

_connection = None


def get_connection():
    return sqlite3.connect(PATH_DATABASE)
