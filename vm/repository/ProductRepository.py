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

    def show_all(self):
        query = """
            SELECT id, name, price FROM products
        """
        query = self.connection.execute(query)
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

        return tabulate(result, headers='keys', tablefmt='sqlite')

    def add(self, product: Product):
        pass

    def get(self, repository):
        pass
