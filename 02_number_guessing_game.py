# Number Guessing Game

import random

print("     Number Guessing Game")
print("===================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try Again.")

    elif guess > secret_number:
        print("Too High! Try Again.")

    else:
        print("\n Congratulations!")
        print("You guessed the correct number.")
        print("Total Attempts:", attempts)
        break

print("\nThank you for playing!")