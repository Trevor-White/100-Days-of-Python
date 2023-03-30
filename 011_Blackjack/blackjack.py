from deck import deck, deal_card
import random
from time import sleep

LINE = "--------------------"

values = {"A": 11, "T": 10, "K": 10, "Q": 10, "J": 10}


def card_value(card):
    if card[0:1] in values:
        return int(values[card[0:1]])
    else:
        return int(card[0:1])


def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[0:1] == "A":
            aces += 1
        value += card_value(card)
    if 21 < value < 32 and aces >= 1:
        value -= 10
    elif 31 < value < 42 and aces >= 2:
        value -= 20
    elif 41 < value < 52 and aces >= 3:
        value -= 30
    elif 51 < value < 62 and aces == 4:
        value -= 40
    return value


# Calculate the value of the cpu hand to show the player
# This will remove the second card value from the calculation
def hand_value_cpu(hand):
    value = 0
    card_num = 0
    for card in hand:
        if card_num == 1:
            value += 0
        else:
            value += card_value(card)
        card_num += 1
    return value


# Deal starting hand to Player
player_hand = []
player_hand.append(deal_card())
player_hand.append(deal_card())

# Deal starting hand to CPU
cpu_hand = []
cpu_hand.append(deal_card())
cpu_hand.append(deal_card())

# Calculate value of each players hand
player_hand_value = hand_value(player_hand)
cpu_hand_value = hand_value(cpu_hand)


# Show starting cards
def show_player_hand(hand):
    visible_hand = []
    for card in hand:
        if card[0:1] == "T":
            visible_hand.append(int(values[card[0:1]]))
        elif card[0:1] in values:
            visible_hand.append(card[0:1])
        else:
            visible_hand.append(int(card[0:1]))
    return visible_hand


# Show CPU cards with second card hidden
def show_cpu_hand(hand):
    visible_hand = []
    card_num = 0
    for card in hand:
        if card_num == 1:
            visible_hand.append("?")
        elif card[0:1] == "T":
            visible_hand.append(int(values[card[0:1]]))
        elif card[0:1] in values:
            visible_hand.append(card[0:1])
        else:
            visible_hand.append(int(card[0:1]))
        card_num += 1
    return visible_hand


print(f"\n\nPlayer hand: {show_player_hand(player_hand)} | {hand_value(player_hand)}\n")
print(f"CPU hand: {show_cpu_hand(cpu_hand)} | {hand_value_cpu(cpu_hand)}\n")
print(LINE)


while True:
    hit = input("Would you like to hit (y/n)?")
    if hit == "n":
        print(f"Player stands on {hand_value(player_hand)}\n\n")
        break
    elif hit == "y":
        player_hand.append(deal_card())
        print(
            f"Player hand: {show_player_hand(player_hand)} | {hand_value(player_hand)}"
        )
        if hand_value(player_hand) > 21:
            hit = "n"
            print("BUST...")
            break

print("CPU Reveals it's hidden card...")
print(f"CPU Hand: {show_player_hand(cpu_hand)}\n")
sleep(1)

while hand_value(cpu_hand) < 17:
    print(f"CPU hits")
    cpu_hand.append(deal_card())
    sleep(1)
    if hand_value(cpu_hand) > 21:
        print("CPU Busts...")
    else:
        print(f"CPU hand: {show_player_hand(cpu_hand)} | {hand_value(cpu_hand)}\n")

cpu_hand_value = hand_value(cpu_hand)
player_hand_value = hand_value(player_hand)

sleep(1)

print(f"CPU has {cpu_hand_value} | You have {player_hand_value}")
print(LINE)

sleep(1)

if (player_hand_value > cpu_hand_value) and (player_hand_value <= 21):
    print("You Win!")
elif (cpu_hand_value > 21) and (player_hand_value <= 21):
    print("You Win!")
elif player_hand_value == cpu_hand_value:
    print("Push...")
else:
    print("You Lose!")
