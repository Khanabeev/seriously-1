import sqlite3
import pandas as pd
from abc import ABC
from tabulate import tabulate
from vm.config import PATH_DATABASE
from vm.models.Product import Product

from vm.repository.AbstractRepository import AbstractRepository


def get_connection():
    return sqlite3.connect(PATH_DATABASE)


class ProductRepository(AbstractRepository, ABC):

    def __init__(self):
        self.connection = get_connection()

    def show_all(self, vending_machine_id):
        stm = "SELECT id, name, price FROM products WHERE id IN (SELECT id FROM product_vending_machine WHERE " \
              "vending_machine_id=?); "

        query = self.connection.execute(stm, (int(vending_machine_id),))
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return tabulate(result, headers='keys', tablefmt='sqlite')

    def update(self, obj):
        pass

    def get(self, product_id: int) -> pd.DataFrame:
        stm = "SELECT id, name, price FROM products WHERE id=?"
        query = self.connection.execute(stm, (product_id,))

        cols = [column[0] for column in query.description]
        return pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')
