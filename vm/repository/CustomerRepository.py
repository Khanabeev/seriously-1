import sqlite3
import pandas as pd
from abc import ABC

from tabulate import tabulate

from vm.config import PATH_DATABASE
from vm.models.Customer import Customer
from vm.repository.AbstractRepository import AbstractRepository
from vm.models.VendingMachine import VendingMachine


def get_connection():
    return sqlite3.connect(PATH_DATABASE)


class CustomerRepository(AbstractRepository, ABC):
    def __init__(self):
        self.connection = get_connection()

    def show_all(self):
        pass

    def first(self):
        stm = """
                    SELECT id, uid, balance FROM customers LIMIT 1
                """
        query = self.connection.execute(stm)
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return result

    def update(self, cus: Customer):
        stm = "UPDATE customers SET balance = ? WHERE uid = ?;"
        self.connection.execute(stm, (int(cus.balance), cus.uid))
        self.connection.commit()
        self.connection.close()

        return
