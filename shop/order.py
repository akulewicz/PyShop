from shop.orderelement import OrderElement
from shop.product import Product
import random


class Order:
    def __init__(self, client_first_name, client_last_name, order_elements = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.calculate_price()
        return total_price

    def print_self(self):
        print("*"*20)
        print(f"Zamówienie złożone przez {self.client_first_name} {self.client_last_name}")
        print(f"Wartość zamówienia: {self.total_price}")
        print("-" * 20)
        print("Zamówione produkty:")
        for element in self.order_elements:
            element.print_self()
        print()
        print("*" * 20)
        print()


def generate_order():
    order_elements = []
    number_of_products = random.randint(1, 10)
    for product_number in range(number_of_products):
        name = f"Produkt-{product_number}"
        product_category = "losowa"
        unit_price = random.randint(1, 70)
        new_product = Product(name, product_category, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(new_product, quantity))
    order = Order(client_first_name="Arkadiusz", client_last_name="Kulewicz", order_elements=order_elements)
    return order
