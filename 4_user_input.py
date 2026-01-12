#accepting user input(Project ex. Madlibs, volume calculator,shopping cart)

#using def something() to make/define a new function yourself
def madlibs_game():
    mood = input("How are you feeling right now?: ")
    place = input("Where are you right now?: ")
    thing = input("What do you see right now?: ")

    print(f"You're feeling {mood}")
    print(f"You're currently at {place} then accidentally bump into {thing}")

def cube_volume():
    edge = float(input("What's the length of the cube's (any) edge?: "))
    total = pow(edge, 3)    #power() function makes the edge variable cubed
    print(f"The volume of your cube would be: {total:.0f}cm^3") #:.0f will not show a decimal portion

def shopping_cart():
    item = input("What do you want to buy right now?: ")
    quantity = int(input("How many would you buy?: "))
    price = float(input("What would the price be?: "))

    total = quantity * price
    print(f"You're currently buying {quantity} {item}(s)")
    print(f"Your total would be ${total}")

cube_volume()