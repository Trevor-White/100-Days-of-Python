import random

print("Welcome to the number guessing game...")
print("You will try to guess a number between 1-100")
mode = input("Choose a dificulty. Type 'Hard' or 'Easy'\n").lower()

if mode == "easy":
    guesses_remaining = 10
else:
    guesses_remaining = 5

number = random.randint(1, 100)


def check_guess(number, guess):
    if guess > number:
        return "too high"
    elif guess < number:
        return "too low"
    else:
        return "Correct!"


while guesses_remaining > 0:
    print(f"you have {guesses_remaining} guesses remaining")
    guess = int(input("Guess a number\n"))
    reply = check_guess(number, guess)
    print(f"\n{guess} is {reply}")

    if reply != "Correct!":
        guesses_remaining -= 1
    else:
        break
