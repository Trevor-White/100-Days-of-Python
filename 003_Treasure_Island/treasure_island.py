# Day 3
# Treasure Island

print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
'''
)

# Print a welcome
print("Welcome to Treasure Island.")
print("You are on a mission to find treasure.")

# Ask if they want to go left or right
direction = input(
    'You are at a cross road, where do you want to go? Type "left" or "right"\n'
).lower()

# If they pick left
if direction == "left":
    swim = input(
        """You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n"""
    ).lower()
    # If they picked swim
    if swim == "swim":
        door = input(
            """You come to three doors, red, yellow, and blue. Which one do you open?\n"""
        ).lower()

        # If they picked yellow
        if door == "yellow":
            print("You win!")

        # If they piecked red
        elif door == "red":
            print("The room was full of fire... Game Over.")

        # If they picked blue
        else:
            print("You enter a room full of monsters...game over")

    # If they picked swim
    else:
        print("The boat never came... game over")

# If they picked right
else:
    print("you fell into a hole - game over")
