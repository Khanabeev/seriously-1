from tabulate import tabulate

from vm.models.vending_machine import VendingMachine
from vm.repository.product_repository import ProductRepository
from vm.repository.vending_machine_repository import VendingMachineRepository


class VendingMachineService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.vm_repository = VendingMachineRepository()
        self.current_vending_machine = self._get_vending_machine()

    def select_product(self, product_id: int):
        product_df = self.get_product(product_id)
        if len(product_df) > 0:
            return product_df
        else:
            raise Exception('Product not exists')

    def show_all_products(self):
        vm_id = self.get_vending_machine_id()
        result = self.product_repository.get_all(vm_id)

        return tabulate(result, headers='keys', tablefmt='sqlite')

    def _get_vending_machine(self):
        vm_df = self.vm_repository.get_vending_machine()
        vm = VendingMachine(uid=vm_df["uid"].values[0], balance=vm_df["balance"].values[0])
        return vm

    def update(self):
        self.vm_repository.update(self.current_vending_machine)

    def add_balance(self, amount: int):
        if amount > 0:
            self.current_vending_machine.balance += amount
            self.update()
        else:
            raise Exception('Amount should be positive number')

    def withdraw_balance(self, amount: int = 0) -> int:
        balance = self.current_vending_machine.balance
        if balance - amount >= 0:
            self.current_vending_machine.balance -= amount
            self.update()
        else:
            raise Exception(f"Not enough balance in Vendor Machine, current balance is: {balance}")

        return self.current_vending_machine.balance

    def is_balance_empty(self) -> bool:
        return self.current_vending_machine.balance <= 0

    def get_current_balance(self) -> int:
        return self.current_vending_machine.balance

    def get_vending_machine_id(self):
        vm_df = self.vm_repository.get_vending_machine(self.current_vending_machine.uid)
        return vm_df["id"].values[0]

    def get_product(self, product_id):
        return self.product_repository.get_product(product_id, self.get_vending_machine_id())
