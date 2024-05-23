from art import logo
print(logo)

def clear():
    print("\n" * 100)

def find_winner(bids):
    max_bid = max(bids.values())
    for bidder, bid in bids.items():
        if bid == max_bid:
            return bidder, bid

bidders = {}
first_round = True

while True:
    if not first_round:
        clear()  # Simulate clearing the screen
    else:
        first_round = False

    print("Welcome to the secret auction program!")
    name = input("What's your name? ")
    bid = float(input("What's your bid? $"))

    # Add bidder and bid to dictionary
    bidders[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders != 'yes':
        break

clear()  # Simulate clearing the screen for the final result

winner, winning_bid = find_winner(bidders)
print(f"The winner is {winner} with a bid of ${winning_bid}.")
