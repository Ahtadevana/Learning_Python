#Making some functions to check the user input

name = input("What is your name?: ")
age = int(input("What is your age?: "))
is_online = True

#making mini def functions to check user's input
def name_check(name):
    if name == "":
        print("You didn't input your name!")
    else:
        print(f"hello, {name}")

def age_check(age):
    if age >= 18:
        print("Access granted!")
    else:
        print("You must be 18+ to sign up!")

def status_check(status):
    if status:
        print("User is online!")
    else:
        print("User is offline!")

name_check(name)
age_check(age)
status_check(is_online)