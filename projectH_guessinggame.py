#Making a quiz type game with list and tuples 
choices = []    #user answer choices
score = 0

questions = (("1. What is the capital of the US?"), 
             ("2. What is the 2nd biggest planet in our solar system?"), 
             ("3. What is the term CS in engineering stands for?"))
options = [["A. Idaho", "B. Washington DC", "C. New Jersey", "D. Wyoming"], 
           ["A. Venus", "B. Mercury", "C. Jupiter", "D. Saturn"], 
           ["A. Computer Science", "B. Central Station", "C. Coming Soon", "D. Carbon steel"]]
key_answer = (("b"), ("d"), ("a"))

for question in questions:
    print(question)

    choice = input("What's your answer: ")
    choices.append(choice)

