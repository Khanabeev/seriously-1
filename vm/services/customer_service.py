from vm.models.customer import Customer
from vm.repository.customer_repository import CustomerRepository
from vm.repository.product_repository import ProductRepository


class CustomerService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()
        self.current_customer = self._get_customer()

    def _get_customer(self) -> Customer:
        cus_df = self.customer_repository.get_customer()
        cus = Customer(uid=cus_df["uid"].values[0], balance=cus_df["balance"].values[0])
        return cus

    def show_info(self) -> str:
        return f"Customer uid: {self.current_customer.uid}\nCustomer balance: {self.current_customer.balance}"

    def update(self) -> None:
        self.customer_repository.update(self.current_customer)

    def add_balance(self, amount: int) -> None:
        if amount > 0:
            self.current_customer.balance += amount
            self.update()

    def withdraw_balance(self, amount: int) -> int:
        if self.current_customer.balance >= amount:
            self.current_customer.balance -= amount
            self.update()
        else:
            raise Exception(
                f"Customer balance is not enough, current customer balance is: {self.current_customer.balance}")

        return self.current_customer.balance

    def get_current_balance(self) -> int:
        return self.current_customer.balance

    def add_product(self, product_id) -> None:
        self.customer_repository.add_product(product_id=product_id, customer_id=self.get_customer_id())

    def get_customer_id(self):
        vm_df = self.customer_repository.get_customer(self.current_customer.uid)
        return vm_df["id"].values[0]
