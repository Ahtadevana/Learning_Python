#Making a mood detector program using logical operators 
#Slept well and drink coffee and on weekend == "happy!"

slept_well = False
drank_coffee = False
is_weekend = False

if slept_well and drank_coffee and is_weekend:
    print("You are very very happy :3")
elif slept_well and drank_coffee:
    print("You're happy")
elif slept_well or drank_coffee:
    print("Could've been happier")
elif is_weekend:
    print("it's a bad weekend...")
else:
    print("A. Very. Horrible. Day.")