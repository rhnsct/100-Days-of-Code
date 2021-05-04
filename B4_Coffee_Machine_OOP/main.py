from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


power_off = False

money = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()


while not power_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == 'off':
        power_off = True
    elif choice == 'report':
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)

