import pandas as pd
from vm.database.db_connection import get_connection

from vm.models.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.connection = get_connection()

    def get_all(self):
        pass

    def get_customer(self, uid: str = '') -> pd.DataFrame:
        if uid == '':
            stm = "SELECT id, uid, balance FROM customers LIMIT 1"
            query = self.connection.execute(stm)
        else:
            stm = "SELECT id, uid, balance FROM customers WHERE uid=? LIMIT 1"
            query = self.connection.execute(stm, (uid,))

        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        return result

    def update(self, cus: Customer):
        stm = "UPDATE customers SET balance = ? WHERE uid = ?;"
        self.connection.execute(stm, (int(cus.balance), cus.uid))
        self.connection.close()

    def add_product(self, customer_id, product_id):
        stm = "INSERT INTO customer_product (customer_id, product_id, created_at) VALUES (?,?, DATE());"
        self.connection.execute(stm, (int(customer_id), int(product_id)))
        self.connection.close()
