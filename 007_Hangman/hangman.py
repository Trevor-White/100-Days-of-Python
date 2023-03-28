import random
from listofwords import list_of_words
from hangmanart import HANGMANPICS


# Create a function to convert lists to strings
def convert(list):
    word = ""
    for letter in list:
        word += " " + letter
    return word


# List of possible words
word_list = list_of_words

# Select word and creat a list of its letters
chosen_word = random.choice(word_list).upper()
list_of_letters = list(chosen_word)

# Create a variable with a dash for each letter in chosen word
dashify = "_ " * (len(chosen_word))
current_state = dashify.split()

wrong_letters = []
wrong_guess_counter = 0

print(HANGMANPICS[wrong_guess_counter])
print(convert(current_state))

while "_" in current_state:
    change_flag = False
    # Get user's guess
    guess = input("Guess a letter\n").upper()

    if len(guess) > 1:
        print("\nPlease guess only 1 letter at a time")
        change_flag = True

    for count, value in enumerate(list_of_letters):
        if guess == value:
            current_state[count] = guess
            change_flag = True

    if change_flag == False:
        wrong_guess_counter += 1
        if guess in current_state or guess in wrong_letters:
            print("\nYou already guessed that letter...")
        else:
            wrong_letters += guess
            print("\nThat letter is not in the word")

    if wrong_guess_counter == 6:
        print("\nGAME OVER")
        print(f"Wrong Letters Guessed: {convert(wrong_letters)}")
        print(HANGMANPICS[wrong_guess_counter])
        print(convert(current_state))
        print("You Died\n")
        print(f"The word was: {chosen_word}\n")
        break

    print(f"\nWrong Letters Guessed: {convert(wrong_letters)}")
    print(HANGMANPICS[wrong_guess_counter])
    print(convert(current_state))

if "_" not in current_state:
    print("YOU WON\n")
