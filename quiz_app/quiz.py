print("Welcome to the Quiz App!")

score = 0

# Question 1
answer = input("Q1: What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("Q2: Which planet is closest to the Sun? ")
if answer.lower() == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("Q3: Who is known as the Father of Computers? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("\nQuiz Completed!")
print("Your Final Score:", score, "/ 3")
