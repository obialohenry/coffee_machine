from resources import MENU
from resources import resources

serve = True
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

while serve:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"
              f"\nMoney: ${money}")
    elif user_input == "off":
        serve = False
    elif user_input == "espresso":
        if water < MENU[user_input]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif coffee < MENU[user_input]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarters = (int(input("how many quarters? : ")) * 0.25)
            dimes = (int(input("how many dimes? : ")) * 0.10)
            nickles = (int(input("how many nickles? : ")) * 0.05)
            pennies = (int(input("how many pennies? : ")) * 0.01)
            cost = quarters + dimes + nickles + pennies
            if cost < MENU[user_input]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif cost > MENU[user_input]["cost"]:
                change = round((cost - MENU[user_input]["cost"]),2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
                water -= MENU[user_input]["ingredients"]["water"]
                coffee -= MENU[user_input]["ingredients"]["coffee"]
                money += MENU[user_input]["cost"]
            else:
                print(f"Here is your {user_input} ☕️. Enjoy!")
                water -= MENU[user_input]["ingredients"]["water"]
                coffee -= MENU[user_input]["ingredients"]["coffee"]
                money += MENU[user_input]["cost"]




        
