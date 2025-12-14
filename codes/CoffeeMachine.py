MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20.80,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30.20,
    }
}

resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
}

Tmoney = {"rupee": 0,
         "paise": 0}
TotalMoney = 0
drink = "0"

def Enough(drink):
    try:
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Not enough Water")
            return 0
    except:
        return 1
    try:
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Not enough milk")
            return 0
    except:
        return 1
    try:
        if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Not enough coffee")
            return 0
        else:
            return 1
    except:
        return 1

def Inventory(drink):
    Nresources = {}
    try:
        Nresources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
    except:
        Nresources["water"] = resources["water"]
    try:
        Nresources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    except:
        Nresources["milk"] = resources["milk"]
    try:
        Nresources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    except:
        Nresources["coffee"] = resources["coffee"]
    return Nresources

def choice(drink):
    money = {}
    money["rupee"] = 0
    money["paise"] = 0
    MoneyNeeded = 0
    if drink == "r":
        print("Resources in Machine:")
        print(f"""Water: {resources["water"]} ml
Milk: {resources["milk"]} ml
Coffee: {resources["coffee"]} g
Earning: {round(TotalMoney, 2)} Rs\n""")
        return [resources, money]
    if drink == "off":
        print("Machine ShutDown")
        return [resources, money]
    if drink == "1":
        drink = "espresso"
    elif drink == "2":
        drink = "latte"
    elif drink == "3":
        drink = "cappuccino"
    else:
        print("Wrong Choice")
        return [resources, money]
    MoneyNeeded = MENU[drink]["cost"]
    [Nresources, money] = Action(MoneyNeeded, drink)
    return [Nresources, money]

def Action(MoneyNeeded,drink):
    money = {}
    print("Enter money")
    money["rupee"] = int(input("Rupees: "))
    money["paise"] = int(input("Paise: "))
    if (money["rupee"] + money["paise"] / 100) == MoneyNeeded:
        what = Enough(drink)
        if what == 1:
            print(f"\n Enjoy Your {drink}\n")
            Nresources = Inventory(drink)
            return [Nresources, money]
        else:
            money["rupee"] = 0
            money["paise"] = 0
            return [resources, money]
    elif (money["rupee"] + money["paise"] / 100) > MoneyNeeded:
        what = Enough(drink)
        if what == 1:
            Balance = round((money["rupee"] + money["paise"] / 100) - MoneyNeeded, 2)
            money["rupee"] = MoneyNeeded % 100
            money["paise"] = MoneyNeeded / 100
            print(f"Your Change is {Balance}")
            print(f"\n Enjoy Your {drink}\n")
            Nresources = Inventory(drink)
            return [Nresources, money]
        else:
            print(f"Take your {(money["rupee"] + money["paise"] / 100)} Rs back\n")
            money["rupee"] = 0
            money["paise"] = 0
            return [resources, money]
    else:
        print("\nNot enough Money")
        print(f"Take your {(money["rupee"] + money["paise"] / 100)} Rs back\n")
        money["rupee"] = 0
        money["paise"] = 0
        return [resources, money]


while drink != "off":
    drink = input(f"""MENU: Enter 1,2,3
    1: espresso     -> {MENU["espresso"]["cost"]} Rs
    2: latte        -> {MENU["latte"]["cost"]} Rs
    3: cappuccino   -> {MENU["cappuccino"]["cost"]} Rs\n""").lower()
    [Nresources, money] = choice(drink)
    resources = Nresources
    TotalMoney += (money["rupee"] + money["paise"] / 100)






















