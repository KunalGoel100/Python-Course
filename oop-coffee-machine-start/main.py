from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

kun = Menu()
resource = CoffeeMaker()
money = MoneyMachine()
# print(kun.get_items())
latte = kun.find_drink("latte")

# print(latte.ingredients)

# print("Enter choice of coffee:")
Choice = 'one'
while Choice != 'off':
    Choice = input(f"{kun.get_items()}\n")
    if Choice == "r":
        resource.report()
        money.report()
    elif Choice == "off":
        print("Machine Shutdown")
    else:
        ChoiceDetail = kun.find_drink(Choice)
        Available = resource.is_resource_sufficient(ChoiceDetail)
        if Available == True:
            print(f"The cost of {Choice} is: {ChoiceDetail.cost} Rs")
            MoneyOk = money.make_payment(ChoiceDetail.cost)
            if MoneyOk == True:
                resource.make_coffee(ChoiceDetail)


