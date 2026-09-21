# Rock Paper Scissors Game

import random

print("     Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter Rock, Paper, or Scissors: ").lower()

print("\nYou chose:", user)
print("Computer chose:", computer)

if user not in choices:
    print("\nInvalid choice! Please enter Rock, Paper, or Scissors.")

elif user == computer:
    print("\n🤝 It's a Tie!")

elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("\n🎉 Congratulations! You Win!")

else:
    print("\n😔 Computer Wins!")

print("\nThanks for playing!")