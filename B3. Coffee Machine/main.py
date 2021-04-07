from dictionaries import resources
from dictionaries import MENU
import os

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25
money = 0
power = True


def clear():
    os.system('clear')


def insert_coins(price_drink, coffee):
    p = int(input("How many pennies would you like to insert? "))
    n = int(input("How many nickels would you like to insert? "))
    d = int(input("How many dime would you like to insert? "))
    q = int(input("How many quarters would you like to insert? "))

    total_inserted = (p * PENNY) + (n * NICKEL) + (d * DIME) + (q * QUARTER)
    total_inserted_formatted = "{:.2f}".format(total_inserted)
    change = total_inserted - price_drink
    change_formatted = "{:.2f}".format(change)
    if change > 0:
        print(f"Here's your change of ${change_formatted}. Enjoy your {coffee}.")
    elif change == 0:
        print(f"Enjoy your {coffee}.")
    else:
        print(f"You did not insert enough coins, ${total_inserted_formatted}, try again.")


def report():
    formatted_money = "{:.2f}".format(money)
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Milk: {resources['milk']}ml")
    print(f"Money: ${formatted_money}")


def report_resources(drink):
    resources['water'] -= MENU[drink.capitalize()]['water']
    resources['coffee'] -= MENU[drink.capitalize()]['coffee']
    resources['milk'] -= MENU[drink.capitalize()]['milk']
    drink_cost = MENU[drink.capitalize()]['price']

    if resources['water'] < 0:
        print("Not enough water. Turn off and replace.")
        return False
    elif resources['coffee'] < 0:
        print("Not enough coffee. Turn off and replace.")
        return False
    elif resources['milk'] < 0:
        print("Not enough milk. Turn off and replace.")
        return False
    else:
        print(f"The drink costs ${drink_cost}.")
        return drink_cost


while power:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == 'espresso' or prompt == 'latte' or prompt == 'cappuccino':
        report_check = report_resources(prompt)
        if report_check:
            insert_coins(report_check, prompt)
            clear()
            money += report_check
            report()

    elif prompt == 'report':
        clear()
        report()

    elif prompt == 'off':
        power = False
        clear()
        print('Powering down.')



