class Product:
    def __init__(self, name, product_category, unit_price):
        self.name = name
        self.product_category = product_category
        self.unit_price = unit_price

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.product_category == other.product_category and
                self.unit_price == other.unit_price)

    def __str__(self):
        return f"Nazwa produktu: {self.name}, kategoria {self.product_category}, cena jednostkowa: {self.unit_price} PLN."


