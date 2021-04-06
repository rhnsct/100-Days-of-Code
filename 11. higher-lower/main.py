from game_data import data
from art import logo, vs
import random
import os



PEOPLE_LIST = data
challenger_dictionary = {'a': '', 'b': '',}

def clear():
    os.system('clear')
    print(logo)

#select random challenders while making sure it's not the same person or that they have the same number of followers
def random_person(a):
    challenger_dictionary[a] = random.choice(PEOPLE_LIST)
    if challenger_dictionary['a'] != '' and challenger_dictionary['b'] != '':

        while challenger_dictionary['a']['follower_count'] == challenger_dictionary['b']['follower_count']:
            
            challenger_dictionary['b'] = random.choice(PEOPLE_LIST)
    
def compare_followers():
    '''Compare number of followers between two challangers'''
    get_followers_A = challenger_dictionary['a']['follower_count']
    get_followers_B = challenger_dictionary['b']['follower_count']
    if get_followers_A > get_followers_B:
        return 'a'
    else:
        return 'b'

def print_info(i):
    '''Prints the information of the challenger inputted'''
    name = challenger_dictionary[i]['name']
    description = challenger_dictionary[i]['description']
    country = challenger_dictionary[i]['country']
    print(f"{i.upper()}: {name}, {description} from {country} ")


def game():
    
    points = 0
    gameover = False
    random_person('a')
    print(logo)


    while gameover == False:

        
        random_person("b")
        print_info("a")
        print(vs)
        print_info("b")
        answer = input("\nWho do you think has more followers 'A' or 'B'? ").lower()

        if compare_followers() == answer:
            points += 1
            challenger_dictionary['a'] = challenger_dictionary['b']
            clear()
            print(f"Your current score is {points}!")
    
        else:
            gameover = True
            clear()
            print(f"Game Over! Final score was {points}")
    
    if input("Would you like to play again? 'Y' or 'N': ").lower() == 'y':
        
        os.system('clear')
        game()
    
game()



