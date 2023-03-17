# Day 2
# Tip Calculator


print("Welcome to the tip calculator...")

# Ask for the total amount of the bill
total = float(input("What was the total bill? $"))

# Ask how many ways the bills should be split
split = int(input("How many ways to split the bill? "))

# Ask what percentage tip they would like to give
percent = float(input("What percantage tip would you like to give? "))

# Calculate the payment per person
payment = round((total * (percent / 100) + total) / split, 2)

# Print the payment for each person
print(f"Each person should pay: ${payment:.2f}")
