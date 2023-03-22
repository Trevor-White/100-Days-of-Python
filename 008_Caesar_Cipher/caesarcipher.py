from encryption import encrypt, decrypt

LINE = "- - - - - - - - - - - - - - - - - - - -"

print(f"\n{LINE}\nWelcome to the Caesar Cipher\n{LINE}\n")
print("What would you like to do?")
choice = input(" 1 - Encrypt a message \n 2 - Decrypt a message \n 3 - Quit\n ")

while True:
    if choice == "1":
        message = str(input("\nPlease enter the message you would like to encrypt:\n "))
        key = int(input("\nPlease enter the key you would like to use (1-15):\n Key:"))
        print(f"\nYour encrypted message is:\n\n {encrypt(message, key)}\n")
        print(f"{LINE}\nWhat would you like to do now?")
        choice = input(" 1 - Encrypt a message \n 2 - Decrypt a message \n 3 - Quit\n ")

    if choice == "2":
        message = str(input("\nPlease enter the message you would like to decrypt:\n"))
        key = int(input("\nPlease enter the key you would like to use (1-15):\n Key: "))
        print(f"\nYour decrypted message is:\n\n {decrypt(message, key)}\n\n")
        print(f"{LINE}\nWhat would you like to do now?")
        choice = input(" 1 - Encrypt a message \n 2 - Decrypt a message \n 3 - Quit\n ")

    if choice != "1" and choice != "2":
        print(f"{LINE}\nThank you for using the Caesar Cipher!\n{LINE}")
        break
