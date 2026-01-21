import random

options = ("rock", "paper", "scissor")
opponent = random.choice(options)
tries = 0

while True:
    hand = input("Rock, paper, or scissors?: ")

    if hand == "q":
        break
    elif hand == "rock":
        if opponent == "rock":
            print("TIE")
        elif opponent == "paper":
            print("YOU LOSE!")
        else:
            print("YOU WIN!")
    elif hand == "paper":
        if opponent == "rock":
            print("YOU WIN!")
        elif opponent == "paper":
            print("TIE")
        else:
            print("YOU LOSE!")
    elif hand == "scissor":
        if opponent == "rock":
            print("YOU LOSE!")
        elif opponent == "paper":
            print("YOU WIN!")
        else:
            print("TIE")
    else:
        print("What is that hand form? Try again.")

    print(f"{hand} vs {opponent}")
    input("Play again?(q to quit)")