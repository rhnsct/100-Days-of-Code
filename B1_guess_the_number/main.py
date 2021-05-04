from art import logo
from random import randint
import os

EASY_LIVES = 10
HARD_LIVES = 5

def clear():
    os.system('clear')
    print(logo)

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    if difficulty == 'easy':
        return EASY_LIVES
    else:
        return HARD_LIVES

def check_answer(guess, the_number, num_lives):
    if guess > the_number:
        print("Too high.")
        return num_lives - 1
    elif guess< the_number:
        print("Too low.")
        return num_lives - 1
    else:
        print(f"You win! The answer was {the_number}.")



def game_on():
    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    num_lives = set_difficulty()
    the_number = randint(1, 100)
    guess = 0

    while guess != the_number:
        
        print(f"You have {num_lives} attempts remaining.")
        guess = int(input("Guess a number: "))
        clear()
        print(f"You guessed {guess}.")
        num_lives = check_answer(guess, the_number, num_lives)
        
        
        if num_lives == 0:
            print("You've run out of lives, you lose!")
            return
        
        
    if input("\nWould you like to go again, type 'y' for yes and 'n' for no: ") == 'y':
        os.system('clear')
        game_on()
    else:
        print("\nGoodbye!")

game_on()

