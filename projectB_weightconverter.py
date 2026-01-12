#Making a weight converter program in Python
unit = input("What standard unit of mass do you use(Kg/Lbs)?: ").lower()
weight = float(input(f"What's your current weight?({unit}): "))

def convert_weight(weight, unit):
    if unit == "lbs":
        total = weight * 0.453592
        unit = "Kg"

    elif unit == "kg":
        total = weight * 2.20462
        unit = "Lbs"

    else:
        print("{unit} is invalid! Unit of mass must be (Kg/Lbs)")
    return total, unit

result, unit = convert_weight(weight, unit)
print(f"Converted successfully! Your result is: {result} {unit}")