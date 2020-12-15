from shop.apple import Apple
from shop.order import generate_order

if __name__ == '__main__':

    order_one = generate_order()
    order_one.print_self()
    green_apple = Apple("Ladne jabłka", "L", 6)
    print(green_apple.apples_total_price(6))