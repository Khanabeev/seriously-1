import sqlite3

from setuptools import setup, find_packages
from vm.config import PATH_SQLITE_CREATE, PATH_SQLITE_SEED, PATH_DATABASE


def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name='vm',
    version='0.1',
    packages=find_packages(),
    include_package_date=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        vm=vm.cli:cli
    """,
)

try:
    sqlite_connection = sqlite3.connect(PATH_DATABASE)

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
