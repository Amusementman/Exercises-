#We have a dictionary storing items in the costco foodcourt menu.

menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def items_prices(item, price):
    menu.update(item, price)

items_prices(item = "watermelon", price = 0.78)
print(str(menu))

#Create a function that has two parameters, item and price, and adds that item and price into the menu dictionary.
#Call the function with an item and price of your choosing and then print out the dictionary to
#test if your function worked.

#NOT DONE
