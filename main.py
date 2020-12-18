from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import LOGO

# variables
coffee_maker = CoffeeMaker()
menu = Menu()
menu_items = menu.get_items().replace("/", " ")
menu_items_list = menu_items.split()
print(menu_items_list)
is_on = True
while is_on:
    print(LOGO)
    print("What would you like ?\n",menu_items)
    user_input = input()
    if user_input == "Off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
    elif user_input in menu_items_list:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
