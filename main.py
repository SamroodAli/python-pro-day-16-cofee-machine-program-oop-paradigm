from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import LOGO

# variables
COFFEE_MAKER = CoffeeMaker()
MENU = Menu()
MONEY_MACHINE = MoneyMachine()
menu_items = MENU.get_items().replace("/", " ")
menu_items_list = menu_items.split()
print(menu_items_list)
is_on = True
while is_on:
    print(LOGO)
    print("What would you like ?\n", menu_items)
    user_input = input().lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        COFFEE_MAKER.report()
    elif user_input in menu_items_list:
        drink = MENU.find_drink(user_input)
        if COFFEE_MAKER.is_resource_sufficient(drink):
            print(f"That will be ${drink.cost}")
            try:
                payment_success = MONEY_MACHINE.make_payment(drink.cost)
                if payment_success:
                    COFFEE_MAKER.make_coffee(drink)
            except ValueError:
                print("sorry, error in inserting coins. Money refunded")
