import sqlite3
import os.path

from vm.config import PATH_SQLITE_SEED, PATH_SQLITE_CREATE, PATH_DATABASE
from vm.database.db_connection import get_connection

if not os.path.isfile(PATH_DATABASE):
    try:
        sqlite_connection = get_connection()

        cursor = sqlite_connection.cursor()

        with open(PATH_SQLITE_CREATE, 'r') as sqlite_file:
            sql_script = sqlite_file.read()
            cursor.executescript(sql_script)

        with open(PATH_SQLITE_SEED, 'r') as sqlite_file:
            sql_script = sqlite_file.read()
            cursor.executescript(sql_script)

        cursor.close()

    except sqlite3.Error as error:
        print("Error during connection to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
        print('SQLite database successfully installed')

else:
    print('Database already exists')
