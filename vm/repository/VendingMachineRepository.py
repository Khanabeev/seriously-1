import sqlite3
import pandas as pd
from abc import ABC

from tabulate import tabulate

from vm.config import PATH_DATABASE
from vm.repository.AbstractRepository import AbstractRepository


def get_connection():
    return sqlite3.connect(PATH_DATABASE)


class VendingMachineRepository(AbstractRepository, ABC):
    def __init__(self):
        self.connection = get_connection()

    def show_all(self):
        query = """
            SELECT * FROM vending_machines
        """
        query = self.connection.execute(query)
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return tabulate(result, headers='keys', tablefmt='sqlite')

    def add(self, obj):
        pass

    def get(self, obj_id):
        pass

    def first(self):
        query = """
                    SELECT id, uid, balance FROM vending_machines LIMIT 1
                """
        query = self.connection.execute(query)
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return result
