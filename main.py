from resources import MENU
from resources import resources

serve = True
money = 0

def process_coins()-> float:
    """Sum total of coins inputted by a user."""
    print("Please insert coins.")
    quarters = (int(input("how many quarters? : ")) * 0.25)
    dimes = (int(input("how many dimes? : ")) * 0.10)
    nickles = (int(input("how many nickles? : ")) * 0.05)
    pennies = (int(input("how many pennies? : ")) * 0.01)
    return quarters + dimes + nickles + pennies

def is_resource_sufficient(an_ordered__drink_resource:dict)-> bool:
    """returns True if there are enough resources in the shop to make a particular coffee drink.
       gives user feedback if resources is not enough.
    """
    for item in an_ordered__drink_resource:
        if resources[item] < an_ordered__drink_resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def check_transaction_status(user_payment:float,drink_cost:float,an_ordered_resource:dict):
    """Checks if a user transaction is/is not a success, and give user feedback, and update the shops resources."""
    if user_payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round((user_payment - drink_cost), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_input} ☕️. Enjoy!")
        for item in an_ordered_resource:
            resources[item] -= an_ordered_resource[item]
        global money
        money += MENU[user_input]["cost"]



# A while loop to keep the services on, until it is explicitly turned off(for maintenance or anything😂).
while serve:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g"
              f"\nMoney: ${money}")
    elif user_input == "off":
        serve = False
    else:
        coffee_drink = MENU[user_input]
        cost_of_drink = MENU[user_input]["cost"]
        if is_resource_sufficient(coffee_drink["ingredients"]):
            payment = process_coins()
            check_transaction_status(user_payment=payment,drink_cost=cost_of_drink,an_ordered_resource=coffee_drink["ingredients"])







        
