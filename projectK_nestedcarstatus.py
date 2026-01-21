import sys
is_running = False

while True:
    car = input("> ").lower()

    if car == "q" or car == "quit":
        break
    elif car == "start":
        if is_running:
            print("You already started the car! <!>")
        else:
            is_running = True
            print("Car has started!")
    elif car == "stop":
        if not is_running:
            print("You already stopped the car! <!>")
        else:
            is_running = False
            print("Car is stopped!")
    elif car == "help":
        print("""
start - starts the car
stop - stops the car
q(quit) - to quit
              """)
    else:
        print("I dont understand that")

if is_running:
    print("-----\nYou left the car running")
else:
    print("-----\nYour car is parked")