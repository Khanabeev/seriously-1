from vm.models.Customer import Customer
from vm.repository.CustomerRepository import CustomerRepository
from vm.repository.ProductRepository import ProductRepository


class CustomerService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()
        self.current_customer = self.__get_first_customer()

    def __get_first_customer(self) -> Customer:
        cus_df = self.customer_repository.first()
        cus = Customer(uid=cus_df["uid"].values[0], balance=cus_df["balance"].values[0])
        return cus

    def show_info(self):
        return f"Customer uid: {self.current_customer.uid}\nCustomer balance: {self.current_customer.balance}"

    def update(self):
        self.customer_repository.update(self.current_customer)
