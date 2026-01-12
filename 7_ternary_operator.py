#   Making a ternary operator!
#   x if condition else y

name = input("What is your name?: ")
age = int(input("What is your age?: "))
is_vip = False
is_senior = True if age >= 60 else False

if name == "Felix" or is_vip:
    print("Full access!")
elif is_senior:
    print("Special Access!")
elif age >= 18:
    print("Access granted as a regular member!")
elif age <= 18:
    print("No ENTRY! Age must be 18+ or become a VIP member")
else:
    print("Invalid somehow") #for troubleshootin shits