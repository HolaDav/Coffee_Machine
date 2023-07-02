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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
machine_on = True


def process_coin():
    print("Please insert coins")
    quarters = int(input("Quarters: "))
    dime = int(input("Dimes: "))
    nickel = int(input("Nickels: "))
    penny = int(input("Pennies: "))
    coin = round((quarters * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01))
    return coin


def enough_coins(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        for remains in resources:
            if ingredient == remains:
                if MENU[coffee]["ingredients"][ingredient] > resources[remains]:
                    global status
                    status = "unsuccessful"
                    print(f"Sorry there is not enough {remains}.\nMoney refunded")
                else:
                    resources[remains] -= MENU[coffee]["ingredients"][ingredient]


def status_successful(coffee):
    print(f"Here is your {coffee_prompt.title()}☕. Enjoy!!")
    global money
    money += MENU[coffee]["cost"]
    print(f"Take your change: ${change}")


while machine_on:
    coffee_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    status = "successful"

    if coffee_prompt == "off":
        machine_on = False

    unit = "ml"
    if coffee_prompt == "report":
        for report in resources:
            if report == "coffee":
                unit = "g"
            print(f"{report}: {resources[report]}{unit}")
        print(f"${money}")

    if coffee_prompt == "espresso":
        profit = process_coin()
        if profit < MENU["espresso"]["cost"]:
            print("Not enough coins!!\nMoney refunded")
        else:
            if profit > MENU["espresso"]["cost"]:
                change = profit - MENU["espresso"]["cost"]
            enough_coins("espresso")
        if status == "successful":
            status_successful("espresso")

    elif coffee_prompt == "latte":
        profit = process_coin()
        if profit < MENU["latte"]["cost"]:
            print("Not enough coins!!!\nMoney refunded")
        else:
            if profit > MENU["latte"]["cost"]:
                change = profit - MENU["latte"]["cost"]
            enough_coins("latte")
        if status == "successful":
            status_successful("latte")

    elif coffee_prompt == "cappuccino":
        profit = process_coin()
        if profit < MENU["cappuccino"]["cost"]:
            print("Not enough coins!!!\nMoney refunded")
        else:
            if profit > MENU["cappuccino"]["cost"]:
                change = profit - MENU["cappuccino"]["cost"]
            enough_coins("cappuccino")
        if status == "successful":
            status_successful("cappuccino")
