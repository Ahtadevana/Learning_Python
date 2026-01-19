#Making concession stand program with menus and their prices
spaces = "-----"
total = 0

print(spaces + "|THE MENU|" + spaces)
menu = {"Popcorn": 6.00,
        "Hot dog": 4.00,
        "Pretzel": 6.00,
        "Chocolate box": 10.00,
        "Soda": 3.00,
        "Water": 1.00}

for key, value in menu.items():
    print(f"{key:15}-> ${value:5}")
print(spaces)

orders = []
while True:
    order = input("What would you like to buy?(q to quit): ").capitalize()
    if order.lower() == "q":
        break
    elif menu.get(order) != None:
        orders.append(order)
    else:
        print("\n<!> Item is unavailable <!>\n")

print(spaces + "|Receipt|" + spaces)
for order in orders:
    total += menu.get(order)
    print(order)
