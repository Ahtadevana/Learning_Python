#Making concession stand program with menus and their prices
spaces = "-----"
total = 0

print(spaces + "|THE MENU|" + spaces)
menu = {"Popcorn": 6.00,
        "Hot dog": 4.00,
        "Pretzel": 6.00,
        "Chocolate": 10.00,
        "Soda": 3.00,
        "Water": 1.00}

for key, value in menu.items(): #prints a dict into a readable lists
    print(f"{key:15}-> ${value:5.2f}")
print(spaces)

orders = []
while True:
    order = input("What would you like to buy?(q to quit): ").capitalize()
    if order.lower() == "q":
        break
    elif menu.get(order) != None:   #.get() takes the key and it returns a value (without erasing them)
        orders.append(order)
    else:   #mitigates errors if None value shows up
        print("\n<!> Item is unavailable <!>\n")

print(spaces + "|Receipt|" + spaces)
for order in orders:
    total += menu.get(order)    #ALWAYS REMEMBER, .get() takes a key, then returns it into a value
    print(order)

print(spaces + f"\nYour total is: ${total:.2f}")