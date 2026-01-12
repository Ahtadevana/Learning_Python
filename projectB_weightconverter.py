#Making a weight converter program in Python
unit = input("What's the unit of mass you use(Kg/Lbs): ").lower()
weight = float(input(f"What's your weight ({unit})?: "))

def convert_weight(weight, factor):
    return weight * factor

if unit == "kg":
    result = convert_weight(weight, 2.20462)
    unit = "Lbs"
elif unit == "lbs":
    result = convert_weight(weight, 0.453592)
    unit = "Kg"
else:
    print(f"{unit} is INVALID! Unit of mass must be Kg/Lbs!")
    exit() #instantly ending the code

print(f"Converted successfully! Your result would be {result:.1f} {unit}")