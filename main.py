class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass

orders = [Order(), Order(), Order(), Order(), Order()]

products = {
    "komputer": Product(),
    "monitor": Product()
}


if __name__ == '__main__':
    red_apple = Apple()
    green_apple = Apple()
    print(f"Czerwone jabłko jest typu {type(red_apple)}.")

