def name_check(name):
    while name == "":
        print("You haven't entered your name!")
        name = input("Enter your name: ")
    return name

def age_check(age):
    while int(age) <= 0:
        print("INVALID. Age must be above zero")
        age = int(input("Enter your age: "))
    return age

name = input("Enter your name: ")
name = name_check(name)

age = int(input("Enter your age: "))
age = age_check(age)

print(f"hello, {name}!")
print(f"You are {age} years old!")