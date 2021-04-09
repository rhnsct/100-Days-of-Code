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
    """"Take inputs for the number of coins of each type and calculate the total
    amount inserted. Return change if there's too much and restart if there's too little."""
    total = int(input("How many pennies would you like to insert? ")) * PENNY
    total += int(input("How many nickels would you like to insert? ")) * NICKEL
    total += int(input("How many dime would you like to insert? ")) * DIME
    total += int(input("How many quarters would you like to insert? ")) * QUARTER
    clear()

    total_formatted = "{:.2f}".format(total)
    change = total - price_drink
    change_formatted = "{:.2f}".format(change)

    if change > 0:
        for item in resources:
            resources[item] -= MENU[coffee.capitalize()][item]
        print(f"Here's your change of ${change_formatted}. Enjoy your {coffee}.")
        return True
    elif change == 0:
        for item in resources:
            resources[item] -= MENU[coffee.capitalize()][item]
        print(f"Enjoy your {coffee}.")
        return True
    else:
        print(f"You did not insert enough coins, ${total_formatted}, try again.")
        return False


def report():
    """"Print the number of resources left in the machine."""
    formatted_money = "{:.2f}".format(money)
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Milk: {resources['milk']}ml")
    print(f"Money: ${formatted_money}")


def report_resources(drink):
    """Check if there is enough to follow through with the
    order based on the input, returning the price of the drink if there is enough resources."""
    drink_cost = MENU[drink.capitalize()]['price']
    order_drink = MENU[drink.capitalize()]
    for item in resources:
        if order_drink[item] > resources[item]:
            print(f"There is not enough {item}")
            return False

    print(f"The drink costs ${drink_cost}.")
    return drink_cost


while power:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == 'espresso' or prompt == 'latte' or prompt == 'cappuccino':
        report_check = report_resources(prompt)
        if report_check > 0:
            if insert_coins(report_check, prompt):
                money += report_check
        report()

    elif prompt == 'report':
        clear()
        report()

    elif prompt == 'off':
        power = False
        clear()
        print('Powering down.')
