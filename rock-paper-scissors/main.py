import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpc = [rock, paper, scissors]

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
choice_int = int(choice)
computer_choice = random.randint(0, 2)

# print(rpc[choice_int] + "\n")
# print("Computer chose:\n\n" + rpc[computer_choice]

# if statement hell
# if choice_int == 0 and computer_choice == 0:
#   print("It's a tie.")
# elif choice_int == 0 and computer_choice == 1:
#   print("You lose.")
# elif choice_int == 0 and computer_choice == 2:
#   print("You win.")
# elif choice_int == 1 and computer_choice == 0:
#   print("You win.")
# elif choice_int == 1 and computer_choice == 1:
#   print("It's a tie.")
# elif choice_int == 1 and computer_choice == 2:
#   print("You lose.")
# elif choice_int == 2 and computer_choice == 0:
#   print("You lose.")
# elif choice_int == 2 and computer_choice == 1:
#   print("You win.")
# else:
#   print("It's a tie.")

#solution

if choice_int >= 3 or choice_int < 0:
  print("Invalid input, You lose.")
else: 
  print(rpc[choice_int] + "\n")
  print("Computer chose:\n\n" + rpc[computer_choice] + "\n")
  if choice_int == 0 and computer_choice == 2:
    print("You win.")
  elif choice_int == 2 and computer_choice == 0:
    print("You lose.")
  elif computer_choice > choice_int:
    print("You lose.")
  elif computer_choice < choice_int:
    print("You win.")
  elif computer_choice == choice_int:
    print("It's a tie.")
