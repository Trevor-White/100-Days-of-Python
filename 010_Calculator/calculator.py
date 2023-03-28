from calcfuncs import add, subtract, mutiply, divide

# Create dictionary mapping the symbols to the functions
operations = {"+": add, "-": subtract, "*": mutiply, "/": divide}

# create varaibles
cont = "y"
first_number = ""
answer = 0

# Main function
while cont == "y":
    if first_number == "":
        first_number = float(input("What is the first number?: "))
    else:
        first_number = answer

    for symbol in operations:
        print(symbol)

    operation = input("Pick an operation: ")

    second_number = float(input("What is the next number?: "))

    answer = operations[operation](first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {answer}")

    cont = input("would you like to continue (y/n)?")

    if cont == "y":
        print(answer)
