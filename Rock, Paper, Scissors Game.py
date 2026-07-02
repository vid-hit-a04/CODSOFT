# Rock, Paper, Scissors Game

import random

print("Welcome to Rock, Paper, Scissors Game!")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please select rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: Computer wins!")
        computer_score += 1

    # Score display
    print("Score -> You:", user_score, "| Computer:", computer_score)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break