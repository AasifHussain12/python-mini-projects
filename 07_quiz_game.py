# Quiz Game in Python

score = 0

print("         PYTHON QUIZ GAME")

print("\nQuestion 1")
answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is New Delhi.")

print("\nQuestion 2")
answer = input("Which programming language are you learning? ")
if answer.lower() == "python":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is Python.")

print("\nQuestion 3")
answer = input("How many days are there in a week? ")
if answer == "7":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is 7.")

print("\nQuestion 4")
answer = input("What is 10 + 5? ")
if answer == "15":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is 15.")

print("\nQuestion 5")
answer = input("Which keyword is used to create a function in Python? ")
if answer.lower() == "def":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is def.")

print("\n===================================")
print("           QUIZ RESULT")
print("===================================")

print("Your Score:", score, "/ 5")

if score == 5:
    print("🏆 Excellent! Perfect Score!")
elif score >= 3:
    print("😊 Good Job!")
else:
    print("📚 Keep Practicing!")

print("\nThank you for playing the Quiz Game!")