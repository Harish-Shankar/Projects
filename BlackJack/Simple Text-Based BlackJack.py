import random

dealer_cards = []
player_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 10))
    if len(dealer_cards) == 2:
        print("The dealer has ", dealer_cards)

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 10))
    if len(player_cards) == 2:
        print("You have ", player_cards)

if sum(dealer_cards) == 21:
    print("The dealer won")
elif sum(dealer_cards) > 21:
    print("The dealer busted")

while sum(player_cards) < 21:
    play = input("Do you want to stay or hit?")
    if play == "hit":
        player_cards.append(random.randint(1, 10))
        print("Your cards are ", player_cards)
        if sum(dealer_cards) <= 16:
            dealer_cards.append(random.randint(1, 10))
    else:
        print("The dealer cards are ", dealer_cards)
        print("Your cards are ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("The dealer won")
        elif sum(dealer_cards) == sum(player_cards):
            print("It is a draw")
        else:
            print("You won")
            break

if sum(player_cards) > 21:
    print("You busted")
elif sum(player_cards) == 21:
    print("You have blackjack! You won")
