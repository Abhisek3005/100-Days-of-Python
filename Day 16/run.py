from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine
Money_Machine = MoneyMachine()
Coffee_Maker = CoffeeMaker()
is_on = True
Coffee_Maker.report()
Money_Machine.report()
menu = Menu()
while is_on:
    option = menu.get_items()
    print(option)
    choice = input(f"What would you like?({option})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Coffee_Maker.report()
        Money_Machine.report()
    else:  
         drink=menu.find_drink(choice)
         #print(drink)
         #print(Coffee_Maker.is_resource_sufficient(drink))
         if Coffee_Maker.is_resource_sufficient(drink) and Money_Machine.make_payment(drink.cost):
        #if Money_Machine.make_payment(drink.cost):
          Coffee_Maker.make_coffee(drink)
            