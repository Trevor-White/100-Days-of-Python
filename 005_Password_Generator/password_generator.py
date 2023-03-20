import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "="]

password_letters = int(input("How many letters would you like in your password?"))
password_symbols = int(input("How many symbols would you like in your password?"))
password_numbers = int(input("How many numbers would you like in your password?"))

password_list = []

# Generate Letters
for i in range(0, password_letters):
    index = random.randint(0, len(letters) - 1)
    char = letters[index]
    password_list.append(char)

# Generate Numbers
for i in range(0, password_numbers):
    index = random.randint(0, len(numbers) - 1)
    char = numbers[index]
    password_list.append(char)

# Generate Symbols
for i in range(0, password_symbols):
    index = random.randint(0, len(symbols) - 1)
    char = symbols[index]
    password_list.append(char)

# Shuffle Chars
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)
