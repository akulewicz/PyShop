class Product:
    def __init__(self, name, product_category, unit_price):
        self.name = name
        self.product_category = product_category
        self.unit_price = unit_price


def print_product(product):
    print(f"Nazwa produktu: {product.name}, kategoria {product.product_category}, cena jednostkowa: {product.unit_price} PLN.")


