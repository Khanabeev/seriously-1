from vm.models.Product import *
from vm.repository.ProductRepository import ProductRepository


class VendingMachine:

    def __init__(self):
        self.product_repository = ProductRepository()

    def add_products(self, product: Product):
        pass

    def remove_product(self, product_id: int):
        pass

    def show_one_product(self, product_id: int):
        pass

    def show_all_products(self):
        return self.product_repository.show_all()
