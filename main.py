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


if __name__ == '__main__':
    red_apple = Apple()
    green_apple = Apple()
    print(f"Czerwone jabłko jest typu {type(red_apple)}.")

