MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
  """Returns true when order can be made,false if ingredients are insufficient"""
  for item in order_ingredients:
   if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True
"""Rerurns the total calculated from coin inserted"""
def process_coin():
   print("Please insert coins")
   total = int(input("how many quarters?:"))*0.25
   total += int(input("how many dimes?:"))*0.1
   total += int(input("how many nickles?:"))*0.05
   total += int(input("how many pennies?:"))*0.01
   return total


def is_transaction_sucessful(money_recieved,drink_cost):
   """return true when payment is accepted ,or false if money is insufficient"""
   if money_recieved >= drink_cost:
      change = round(money_recieved - drink_cost,2)
      print(f"Here is ${change} in change ")
      global profit
      profit += drink_cost
      return True
   else:
      print("Sorry thats not enough money .Money refunded")
      return False
   
def make_cofee(drink_name,order_ingredients):
   """Deduct the required ingredients from the resources"""
   for item in order_ingredients:
      resources[item] -= order_ingredients[item]
   print(f"here is your {drink_name}")  
is_on = True
while is_on:
 choice = input("What would you like? (espresso/latte,cappuccino):\n")
 if choice == "off":
    is_on = False
 elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"cofee:{resources['coffee']}g")
        print(f"money:{profit}")

 else:
    drink = MENU[choice]    
    if is_resource_sufficient(drink["ingredients"]):
       payment = process_coin()
       if is_transaction_sucessful(payment,drink["cost"]):
          make_cofee(choice,drink["ingredients"])