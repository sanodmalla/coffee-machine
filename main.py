from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()

isOn = True

while isOn:
    option = menu.get_items()
    choice = input(f"What would u like to get: {option}  ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



