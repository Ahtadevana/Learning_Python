#Making a simple shopping cart problem using lists

things = []
prices = []
currency = input("Insert your currency: ")

while True:
    thing = input("What do you want to buy (q to quit)?: ")
    if thing.lower() == "q":
        break
    price = float(input(f"What's the price of {thing}?: {currency}"))
    things.append(thing)
    prices.append(price)

print("\n-----\nYour shopping list:")
for i in range(len(things)):
    print(f"{i + 1}. {things[i]}", end=f": {currency}")
    print(f"{prices[i]:.2f}")

total = sum(prices)
print(f"Your total is: {currency}{total:.2f}")