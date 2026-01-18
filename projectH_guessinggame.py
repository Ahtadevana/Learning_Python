#Making a quiz type game with list and tuples 
questions = (("1. What is the capital of the US?"), 
             ("2. What is the 2nd biggest planet in our solar system?"), 
             ("3. What is the term CS in engineering stands for?"), 
             ("4. Which animal has four legs?"))
options = (("A. Idaho", "B. Washington DC", "C. New Jersey", "D. Wyoming"), 
           ("A. Venus", "B. Mercury", "C. Jupiter", "D. Saturn"), 
           ("A. Computer Science", "B. Central Station", "C. Coming Soon", "D. Carbon steel"),
           ("A. Chicken", "B. Ostritch", "C. Cat", "D. T-rex"))
key_answers = (("B"), ("D"), ("A"), ("D"))

choices = []
total_questions = 0
score = 0

for question in questions:  #prints questions
    print("-----------------")
    print(question)
    for option in options[total_questions]: #prints options
        print(option)

    choice = input("Write your answer: ").upper()   #user input
    choices.append(choice)
    
    if choice == key_answers[total_questions]:   #score check
        print("correct!")
        score += 1
    else:
        print("Incorrect!", end=" ")
        print(f"Correct answer: {key_answers[total_questions]}")

    total_questions += 1

print("----- RESULT -----")
print("Your guesses: ", end="")
for choice in choices:
    print(choice, end=" ")

if score != total_questions:
    print("\nThe correct answers: ", end="")
    for answer in key_answers:
        print(answer, end=" ")

score *= 100 / total_questions
print(f"\nYour total score is: {round(score)}%")