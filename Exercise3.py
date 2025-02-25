#We have a grocery list of very healthy items. 
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
print(groceries)

while True:
    removable = input("What would you like to remove? ")
    if removable == "cheez its":
        groceries.remove("cheez its")
        print(groceries)
    elif removable == "nerds gummy clusters":
        groceries.remove("nerds gummy clusters")
        print(groceries)
    elif removable == "doritos":
        groceries.remove("doritos")
        print(groceries)
    elif removable == "cocoa puffs":
        groceries.remove("cocoa puffs")
        print(groceries)
    elif removable == "pepsi":
        groceries.remove("pepsi")
        print(groceries)
    elif removable == "dr. pepper":
        groceries.remove("dr. pepper")
        print(groceries)
    elif removable == "mountain dew":
        groceries.remove("mountain dew")
        print(groceries)
    elif removable == "stop":
        print("Okay!")
        break
    else:
        print("Huhhh??")