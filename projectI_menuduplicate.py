shelf = {"Milk":19.99,
         "Cereal":10.99,
         "Chips":4.99,
         "Soda":2.99}

for key, value in shelf.items():
    print(f"{key:10}${value:.2f}")

total = 0
groceries = []
while True:
    cart = input("What do you want to add?('q' to quit)?: ").capitalize()
    if cart.lower() == "q":
        break
    elif shelf.get(cart) != None:
        groceries.append(cart)
        total += shelf.get(cart)
        print("\nItem has been added to your cart!\n-----")
    else:
        print("-----\n<!> Item is sold out/unavailable <!>\n-----")

print("----- RECEIPT -----")
for product in groceries:
    print(product)
print("----- TOTAL -----")
print(f"total: ${total:.2f}")