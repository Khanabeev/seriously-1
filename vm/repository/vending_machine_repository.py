import pandas as pd
from vm.database.db_connection import get_connection

from tabulate import tabulate
from vm.models.vending_machine import VendingMachine


class VendingMachineRepository:
    def __init__(self):
        self.connection = get_connection()

    def get_all(self):
        stm = "SELECT * FROM vending_machines"
        query = self.connection.execute(stm)
        cols = [column[0] for column in query.description]
        result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        return tabulate(result, headers='keys', tablefmt='sqlite')

    def get_vending_machine(self, uid: str = '') -> pd.DataFrame:
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
