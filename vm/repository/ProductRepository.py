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

    def get_all(self, vending_machine_id):
        stm = "SELECT id, name, price FROM products WHERE id IN (SELECT id FROM product_vending_machine WHERE " \
              "vending_machine_id=?); "

        query = self.connection.execute(stm, (int(vending_machine_id),))
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return result

    def update(self, obj):
        pass

    def get_product(self, product_id, vending_machine_id) -> pd.DataFrame:
        stm = "SELECT id, name, price FROM products WHERE id IN (SELECT id FROM product_vending_machine WHERE " \
              "vending_machine_id=?) AND id=?; "

        query = self.connection.execute(stm, (int(vending_machine_id), int(product_id)))
        cols = [column[0] for column in query.description]
        return pd.DataFrame.from_records(data=query.fetchall(), columns=cols)