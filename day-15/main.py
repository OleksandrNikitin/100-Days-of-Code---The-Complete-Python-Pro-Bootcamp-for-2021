from data import MENU, resources


def format_report(data):
    """Format input data and return its format view"""
    return (
        f"Water: {data['water']}ml\nMilk: {data['milk']}ml\nCoffee: {data['coffee']}g"
    )


def check_resources(drink):
    """Check if machine has enough resources and return boolean"""
    ingredients = MENU[drink]["ingredients"]
    for _ in ingredients:
        if ingredients[_] >= resources[_]:
            print(f"Sorry there is not enough {_}.")
            return False
    return True


def process_coins():
    """Take drink type as an argument and process coins respectively"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    overall_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return overall_sum


def check_transaction(received_money, drink):
    """Take calculated sum, drink type. Check if it enough money. Return boolean"""
    drink_cost = MENU[drink]["cost"]
    if received_money >= drink_cost:
        if received_money > drink_cost:
            print(f"Here is ${round((received_money - drink_cost), 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


money = 0

restart_machine = True

while restart_machine:
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if ask == "off":
        restart_machine = False
    elif ask == "report":
        print(f"{format_report(resources)}\nMoney: ${money}")
    elif (
        ask in MENU and check_resources(ask) and check_transaction(process_coins(), ask)
    ):
        money += MENU[ask]["cost"]
        print(f"Here is your {ask} ☕️. Enjoy!")
        make_coffee(ask)
