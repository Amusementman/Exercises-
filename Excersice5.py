
menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def items_prices(item, price):
    menu.update(item, price)
    item = "Watermelon"
    price = 0.78

items_prices(item, price)
print(str(menu))