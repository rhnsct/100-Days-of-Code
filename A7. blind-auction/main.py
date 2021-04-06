import os
from art import logo

def clear():
    os.system('clear')

bids = {}


def highest_bid():
    highest_bid = 0
    bidder_name = ''
    for name, bid in bids.items():
        if bid > highest_bid:
            bidder_name = name
            highest_bid = bid

    print(logo)
    print(f"The highest bidder was {bidder_name.capitalize()} with ${highest_bid}!")




again = 'yes'
while not again == 'no':
    
    print(logo)
    print("Welcome to the auction.")

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    again = input("Is there any other bidders? 'yes' or 'no' \n").lower()
    clear()

highest_bid()


