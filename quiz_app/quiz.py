print("Welcome to the Quiz App!")

score = 0  # starting score

answer = input("Q1: What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your Score:", score)
