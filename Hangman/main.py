
import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

clear = lambda: os.system('clear')
clear()

chosen_word = random.choice(word_list)
letter_count = len(chosen_word)


blank = []

def blank_print():
    print(f"{' '.join(blank)} \n")

lives = 6
guesses = []
win = 0
victory = False




for empty in range(letter_count):
    blank += "_"

print(logo)

print(stages[lives])

while not victory and lives > 0:
    
    blank_print() 

    guess = input("Guess a letter: ")
    
    clear()
    print(logo)
    
    not_in_guesses = guess not in guesses
    

    
    if not_in_guesses == False:
        print("You've already used this letter!")

    elif guess not in chosen_word:
        lives -= 1
        print("Wrong Letter!")
        print("You have " + f"{lives}" + " lives left.")
        
        
    else:
        for position in range(letter_count):

            letter = chosen_word[position]

            if letter == guess:
                blank[position] = guess
                print("Correct!")
                win += 1
                
    victory = win == letter_count
    
    guesses += guess
    print(stages[lives])



if victory == True:

    print("You win!")  

else:
    print("You lose!") 
    print(f"The word was {chosen_word}.")       

            




