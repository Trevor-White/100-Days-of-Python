# Welcome
print("Welcome to the silent auction")

bidders = {}
while True:
    name = input("What is your name?\n")
    # Get bid
    bid = int(input("What is your bid?\n $"))
    bidders[name] = bid
    # Ask if there are any more bidders
    more_bidders = input("Are there any more bidders (y/n)?\n")
    if more_bidders == "y":
        pass
    else:
        break

print(bidders)

# identify the highest bidder
high_bid = 0
high_bidder = ""
for bidder in bidders:
    if bidders[bidder] > high_bid:
        high_bid = bidders[bidder]
        high_bidder = bidder
    else:
        pass

# print the name of the winner
print(f"The winner is {high_bidder} with a bid of {high_bid}")
