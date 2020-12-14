class Product:
    def __init__(self, name, product_category, unit_price):
        self.name = name
        self.product_category = product_category
        self.unit_price = unit_price


class Order:
    def __init__(self, client_firstname, client_lastname, products = None):
        self.client_firstname = client_firstname
        self.client_lastname = client_lastname
        self.total_price = 0

        if products == None:
            products = []
        self.products = products

        for product in products:
            self.total_price += product.unit_price


class Apple:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


def print_product(product):
    print(f"Nazwa produktu: {product.name}, kategoria {product.product_category}, cena jednostkowa: {product.unit_price} PLN.")


def print_order(order):
    print("*"*20)
    print(f"Zamówienie złożone przez {order.client_firstname} {order.client_lastname}")
    print(f"Wartość zamówienia: {order.total_price}")
    print("-" * 20)
    print("Zamówione produkty:")
    for product in order.products:
        print_product(product)
    print()
    print("*" * 20)
    print()




if __name__ == '__main__':

    products = [
        Product('Komputer', 'elektronika', 1800),
        Product('Monitos', 'elektronika', 800)
    ]

    order_one = Order('Jaś', 'Fasola', products)
    print_order(order_one)
