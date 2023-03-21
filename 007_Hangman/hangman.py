import random

word_list = ["aardvark", "baboon", "camel", "butterfly"]

chosen_word = random.choice(word_list)
list_of_letters = list(chosen_word)

current_state = "_ " * (len(chosen_word))
current_state_list = current_state.split()

print(current_state)
print(current_state_list)

while "_" in current_state_list:
    print(current_state_list)
    guess = input("Guess a letter\n")
    for count, value in enumerate(list_of_letters):
        if guess == value:
            current_state_list[count] = guess
