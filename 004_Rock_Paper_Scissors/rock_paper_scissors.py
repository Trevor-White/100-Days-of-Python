# Day 4
# Rock Paper Scissors Game
import random

# Welcome to the game
print("Let's play Rock, Paper, Scissors...")

# Enter how many rounds the match should be
match_len = int(input("How many rounds would you like to play?\n"))

# Initalize variables
round = 0
cpu_score = 0
user_score = 0

# While the round is less then the number of rounds selected
while round < match_len:

    # The Computer chooses its sign
    computer = random.randint(1, 3)

    # The user inputs their sign
    print("---------------")
    print(f"\nRound {round+1}")
    print(f"Score: You {user_score} | CPU {cpu_score}")
    user = int(input("Choose your sign: (1)Rock (2)Paper (3)Scissors\n"))

    # Error handeling for invalid inputs
    while user not in [1, 2, 3]:
        print("\nInvalid Entry. Please enter 1, 2 or 3")
        user = int(input("Choose your sign: (1)Rock (2)Paper (3)Scissors\n"))

    # create a list of possible signs
    signs = ["Rock", "Paper", "Scissors"]

    computer = signs[computer - 1]
    user = signs[user - 1]

    print(f"\n\nYou picked {user}")
    print(f"The computer picked {computer}")

    if user == computer:
        print("Round Result: Draw")

    # Rock
    if user == "Rock":
        if computer == "Scissors":
            print("Round Result: You Win!")
            user_score += 1
        elif computer == "Paper":
            print("Round Result: You Lose")
            cpu_score += 1

    # Paper
    if user == "Paper":
        if computer == "Rock":
            print("Round Result: You Win!")
            user_score += 1
        elif computer == "Scissors":
            print("Round Result: You Lose")
            cpu_score += 1

    # Scissors
    if user == "Scissors":
        if computer == "Paper":
            print("Round Result: You Win!")
            user_score += 1
        elif computer == "Rock":
            print("Round Result: You Lose")
            cpu_score += 1

    round += 1

print("\n\nFINAL SCORE")
print("------------")
print(f"Computer: {cpu_score}")
print(f"You: {user_score}")

if user_score > cpu_score:
    print("\nYou won the match! You are a Champion!!!\n")
elif user_score < cpu_score:
    print("\nYou lose! Better luck next time...\n")
else:
    print("\nDraw... maybe you should play again?\n")
