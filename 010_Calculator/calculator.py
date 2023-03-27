print("Hello")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mutiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add, "-": subtract, "*": mutiply, "/": divide}


cont = "y"
first_number = ""
answer = 0

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
