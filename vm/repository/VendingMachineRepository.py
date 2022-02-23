import sqlite3
import pandas as pd
from abc import ABC

from tabulate import tabulate

from vm.config import PATH_DATABASE
from vm.repository.AbstractRepository import AbstractRepository
from vm.models.VendingMachine import VendingMachine


def get_connection():
    return sqlite3.connect(PATH_DATABASE)


class VendingMachineRepository(AbstractRepository, ABC):
    def __init__(self):
        self.connection = get_connection()

    def show_all(self):
        stm = """
            SELECT * FROM vending_machines
        """
        query = self.connection.execute(stm)
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return tabulate(result, headers='keys', tablefmt='sqlite')

    def first(self, uid: str = '') -> pd.DataFrame:
        if uid == '':
            stm = "SELECT id, uid, balance FROM vending_machines LIMIT 1"
            query = self.connection.execute(stm)
        else:
            stm = "SELECT id, uid, balance FROM vending_machines WHERE uid=? LIMIT 1"
            query = self.connection.execute(stm, (uid,))

        cols = [column[0] for column in query.description]

        return pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

    def update(self, vm: VendingMachine) -> None:
        stm = "UPDATE vending_machines SET balance = ? WHERE uid = ?;"
        self.connection.execute(stm, (int(vm.balance), vm.uid))
        self.connection.commit()
        self.connection.close()
