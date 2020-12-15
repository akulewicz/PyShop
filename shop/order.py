from shop.product import print_product, Product
import random


class Order:
    def __init__(self, client_first_name, client_last_name, products = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price


def print_order(order):
    print("*"*20)
    print(f"Zamówienie złożone przez {order.client_first_name} {order.client_last_name}")
    print(f"Wartość zamówienia: {order.total_price}")
    print("-" * 20)
    print("Zamówione produkty:")
    for product in order.products:
        print_product(product)
    print()
    print("*" * 20)
    print()


def generate_order():
    products = []
    number_of_products = random.randint(1, 10)
    for product_number in range(number_of_products):
        name = f"Produkt-{product_number}"
        product_category = "losowa"
        unit_price = random.randint(1, 70)
        new_product = Product(name, product_category, unit_price)
        products.append(new_product)
    order = Order(client_first_name="Arkadiusz", client_last_name="Kulewicz", products=products)
    return order
