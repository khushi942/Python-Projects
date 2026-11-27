
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}
active=True

def make_coffee(drink_ingredients):
    for item in resources:
        if item=="money":
            continue
        resources[item]-=drink_ingredients[item]

    return






def transaction_successful(given_money, required_money):
    if given_money<required_money:
        return ""
    else:
        resources["money"]+=required_money
        change=given_money-required_money
        return change





def process_coins():
    print("Please insert coins ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    coin_value=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    return round(coin_value,2)






def check_resources(drink_want):
    # #drink={"water": 200,
    #         "milk": 150,
    #         "coffee": 24,
    #         }
    drink=MENU[drink_want]['ingredients']

    for ingredient in drink:
        # drink[milk]>resources[milk]
        if drink[ingredient]>resources[ingredient]:
            return ingredient, False
    return "",True






def print_report():
    print(f"water: {resources['water']}ml ")
    print(f"milk:{resources['milk']}ml ")
    print(f"coffee:{resources['coffee']}g")
    print(f"money: ${resources['money']}")



while active:

    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino)"
    user_want=input(" What would you like? (espresso/latte/cappuccino)? ").lower()

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_want=='off':
        active=False

    # TODO 3: Print report of all coffee machine resources
    elif user_want=='report':
        print_report()

    elif user_want=='espresso'or user_want=='latte' or user_want=='cappuccino':
        # TODO 4: Check resources sufficient?
        unsufficient_ingredient, sufficient_resource=check_resources(user_want)
        if not sufficient_resource:
            print(f"Not enough {unsufficient_ingredient}")
        else:
            # TODO 5: Process coins.
            total_coins= process_coins()

            #  TODO 6: Check transaction successful?
            extra_money=transaction_successful(total_coins,MENU[user_want]["cost"])

            if extra_money:
                if extra_money>0:
                    print(f"Here is ${extra_money} dollars in change")
                # TODO 7: Make Coffee
                make_coffee(MENU[user_want]["ingredients"])
                print(f"Enjoy your {user_want}")
            else:
                print("That's not enough money. Money refunded")


    else:
        print("Please enter valid choice!")










