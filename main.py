from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import LOGO

# variables
menu = Menu()
menu_items = menu.get_items().replace("/", " ")
is_on = True
while is_on:
    print(LOGO)
    print("What would you like ?\n",menu_items)
    user_input = input()
    is_on = False
