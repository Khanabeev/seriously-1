from vm.models.Product import *
from vm.models.VendingMachine import VendingMachine
from vm.repository.ProductRepository import ProductRepository
from vm.repository.VendingMachineRepository import VendingMachineRepository


class VendingMachineService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.vm_repository = VendingMachineRepository()
        self.current_vending_machine = self.__get_first_vending_machine()

    def add_products(self, product: Product):
        pass

    def remove_product(self, product_id: int):
        pass

    def show_one_product(self, product_id: int):
        pass

    def show_all_products(self):
        return self.product_repository.show_all()

    def __get_first_vending_machine(self):
        vm_df = self.vm_repository.first()
        vm = VendingMachine(uid=vm_df["uid"].values[0], balance=vm_df["balance"].values[0])
        return vm

    def update(self):
        self.vm_repository.update(self.current_vending_machine)

    def add_money(self, amount: int):
        if amount > 0:
            self.current_vending_machine.balance += amount
            self.update()

    def withdraw_money(self) -> int:
        balance = self.current_vending_machine.balance
        self.current_vending_machine.balance = 0
        self.update()

        return balance

    def is_balance_empty(self) -> bool:
        return self.current_vending_machine.balance <= 0

    def get_current_balance(self) -> int:
        return self.current_vending_machine.balance