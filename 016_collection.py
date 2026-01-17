#Trying to see how collection/nested list work
#whether it's tuples inside a list, or tuples inside a tuple
spaces = "-----"
shopping_cart = [["cereal", "milk", "chips"],
                 ["melon", "grapes", "apples"],
                 ["broccoli", "cauliflower", "pumpkin"]]

for collection in shopping_cart:
    for things in collection:
        print(things.capitalize(), end=" ")
    print()
print(spaces)

print(shopping_cart[0][1])  #prints individual things within a list/tuple
                            #depends on the dimension/nesting level (for ex. this is a 2d list)

#tuples inside of a list
shopping_cart_list = [("cereal", "milk", "chips"),
                        ("melon", "grapes", "apples"),
                        ("broccoli", "cauliflower", "pumpkin")]

#tuples inside of a tuple
shopping_cart_tuples = (("cereal", "milk", "chips"),
                        ("melon", "grapes", "apples"),
                        ("broccoli", "cauliflower", "pumpkin"))