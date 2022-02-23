import pandas as pd
from vm.database.db_connection import get_connection


class ProductRepository:

    def __init__(self):
        self.connection = get_connection()

    def get_all(self, vending_machine_id) -> pd.DataFrame:
        stm = "SELECT id, name, price FROM products WHERE id IN (SELECT id FROM product_vending_machine WHERE " \
              "vending_machine_id=?); "

        query = self.connection.execute(stm, (int(vending_machine_id),))
        cols = [column[0] for column in query.description]
        return pd.DataFrame.from_records(data=query.fetchall(), columns=cols, index='id')

    def get_product(self, product_id, vending_machine_id) -> pd.DataFrame:
        stm = "SELECT id, name, price FROM products WHERE id IN (SELECT id FROM product_vending_machine WHERE " \
              "vending_machine_id=?) AND id=?; "

        query = self.connection.execute(stm, (int(vending_machine_id), int(product_id)))
        cols = [column[0] for column in query.description]
        return pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
