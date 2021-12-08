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


def is_resource_sufficent(order_ingredients):
    """Returns True when order can be made and False when ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += money_received
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")




is_on = True

while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])












































# ========================= Solutia mea===============================


# from data import MENU, resources
#
#
# def check_money(user_choice):
#     '''Asks for money and if users inserts more money, gives change and coffee, returns
#      money inserted if not enough is provided'''
#     quarter = float(input("How many quarters?"))
#     dimes = float(input("How many dimes?"))
#     nickles = float(input("How many nickles?"))
#     pennies = float(input("How many pennies?"))
#     sum = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
#
#     if MENU[user_choice]['cost'] > sum:
#         print(f'Not enough money. Here is your money back {sum}')
#         return False
#
#     elif MENU[user_choice]['cost'] < sum:
#         money_back = round(sum - MENU[user_choice]['cost'], 2)
#         print(f'Here is your Change! {money_back}, enjoy your {user_choice}')
#         return True
#
#
# def make_coffee():
#     coffee = True
#     money = 0
#     while coffee:
#         user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if user_choice == 'report':
#             print(resources['water'], resources['milk'], resources['coffee'], money)
#             return resources['water'], resources['milk'], resources['coffee'], money
#
#         if user_choice == 'off':
#             return 0
#         if user_choice == 'espresso' and check_money(user_choice):
#             if resources['water'] < MENU['espresso']['ingredients']['water']:
#                 print('Not enough water')
#                 return 'Not enough water'
#             elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
#                 print('Not enough coffee')
#                 return 'Not enough coffee'
#             else:
#                 resources['water'] -= MENU['espresso']['ingredients']['water']
#                 resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
#                 money += MENU[user_choice]['cost']
#
#         if user_choice == 'latte' and check_money(user_choice):
#             if resources['water'] < MENU['latte']['ingredients']['water']:
#                 print('Not enough water')
#                 return 'Not enough water'
#             elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
#                 print('Not enough coffee')
#                 return 'Not enough coffee'
#             elif resources['milk'] < MENU['latte']['ingredients']['milk']:
#                 print('Not enough milk')
#                 return 'Not enough milk'
#             else:
#                 resources['water'] -= MENU['latte']['ingredients']['water']
#                 resources['coffee'] -= MENU['latte']['ingredients']['coffee']
#                 resources['milk'] -= MENU['latte']['ingredients']['milk']
#                 money += MENU[user_choice]['cost']
#
#         if user_choice == 'cappuccino' and check_money(user_choice):
#             if resources['water'] < MENU['cappuccino']['ingredients']['water']:
#                 print('Not enough water')
#                 return 'Not enough water'
#             elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
#                 print('Not enough coffee')
#                 return 'Not enough coffee'
#             elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
#                 print('Not enough milk')
#                 return 'Not enough milk'
#             else:
#                 resources['water'] -= MENU['cappuccino']['ingredients']['water']
#                 resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
#                 resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
#                 money += MENU[user_choice]['cost']
#
# make_coffee()







































# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 1.1 Check the user’s input to decide what to do next.
# TODO: 1.2 The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
# TODO:


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 2.1 For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
# TODO:

# TODO: 3. Print report.
# TODO: 3.1 When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# TODO:

# TODO: 4. Check resources sufficient?
# TODO: 4.1. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO: 4.2 E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# TODO: 4.3 The same should happen if another resource is depleted, e.g. milk or coffee.
# TODO:

# TODO: 5. Process coins.
# TODO: 5.1 If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# TODO: 5.2 Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO: 5.3 Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# TODO:
# TODO: 6. Check transaction successful?
# TODO: 6.1 Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# TODO: 6.2 But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# TODO: 6.3 If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places
# TODO:
# TODO: 7. Make Coffee.
# TODO: 7.1 If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# TODO: 7.2 Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
