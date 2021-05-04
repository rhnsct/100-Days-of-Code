
import random
import os
from art import logo

def clear():
    os.system('clear')
    print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]


def random_card(hand):
    random_int = random.randint(0, 12)
    random_card = cards[random_int]
    hand.append(random_card)


def calculate_score(hand):
    """Take a list of cards and calculate their score"""

    score = sum(hand)

    if len(hand) == 2 and score == 21:
        return 0
            

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
            
    return score

def compare(user_score, dealer_score):

    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "You lost, the opponent has a blackjack."
    elif user_score == 0:
        return "You win, you have a blackjack!"
    elif user_score > 21:
        return f"Bust! Your score is {user_score}"
    elif dealer_score > 21:
        return f"Dealer went bust! Dealer score is {dealer_score}"
    elif dealer_score > user_score:
        return f"The dealer wins with a score of {dealer_score} over your {user_score}."
    else:
        return f"You win with a score of {user_score} over the dealers {dealer_score}."


def game():
    clear()
    dealer_hand = []
    user_hand = []
    
   
    for _ in range(2):
        random_card(dealer_hand)
        random_card(user_hand)



    end_game = False

    while end_game == False:
        
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f'The players hand is {user_hand}. Current score: {user_score}')
        print(f'The dealers first card {dealer_hand[0]}.')
        
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            end_game = True
        else:
            hit = input("Would you like to 'hit' or 'stay'? ")
            if hit == 'hit':
                random_card(user_hand)
                clear()
            else:
                end_game = True
    
    print(f'The dealers hand is {dealer_hand}.')
        
    if user_score <= 21 and user_score != 0:
        while dealer_score != 0 and dealer_score < 17:
            random_card(dealer_hand)
            dealer_score = calculate_score(dealer_hand)
        clear()
        print(f'The dealers final hand is {dealer_hand}.')
        print(f'The players final hand is {user_hand}.')
    
    
    print("\n" + compare(user_score, dealer_score))

    if input("Would you like to play again 'y' or 'n'? ") == 'y':
        game()

game()