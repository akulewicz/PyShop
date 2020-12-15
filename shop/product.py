class Product:
    def __init__(self, name, product_category, unit_price):
        self.name = name
        self.product_category = product_category
        self.unit_price = unit_price

    def print_self(self):
        print(f"Nazwa produktu: {self.name}, kategoria {self.product_category}, cena jednostkowa: {self.unit_price} PLN.")


