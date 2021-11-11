import resources

stop = False
report = resources.report
choice_of_drink = ""

#To check if there is sufficient resource in the coffee machine
def is_sufficient_resources(drink):
    global report
    if report["water"] >= resources.MENU[drink]["ingredients"]["water"]:
        if report["coffee"] >= resources.MENU[drink]["ingredients"]["coffee"]:
            if report["milk"] >= resources.MENU[drink]["ingredients"]["milk"]:
                return True
    return False

def make_coffee(drink, pennies, nickel, dimes, quarters):
    is_made = False
    total_cost = (pennies * 0.01) + (0.05 * nickel) + (0.10 * dimes) + (0.25 * quarters)
    print(f"Total amount user paid is: {total_cost}")
    if total_cost >=  resources.MENU[drink]["cost"]:
        is_made = True
        report["water"] -= resources.MENU[drink]["ingredients"]["water"]
        report["coffee"] -= resources.MENU[drink]["ingredients"]["coffee"]
        report["milk"] = resources.MENU[drink]["ingredients"]["milk"]
        report["money"] += resources.MENU[drink]["cost"]
    return is_made

#To get the necessary input from the user
def get_input():
    global stop
    global choice_of_drink

    choice_of_drink = input("What would you like to have (espresso/latte/cappuccino): ")
    if choice_of_drink == 'stop':
        stop = True
    elif choice_of_drink == 'report':
        print(report)
    else:
        is_sufficient = is_sufficient_resources(choice_of_drink)
        if not is_sufficient:
            print("Sorry this coffee is not available :(((")
        else :    
            print("Enter coins !!!")
            quarters = int(input("Enter number of quarters: "))
            dimes = int(input("Enter number of dimes: "))
            nickles = int(input("Enter number of nickels: "))
            pennies = int(input("Enter number of pennies: "))
            is_made = make_coffee(choice_of_drink, pennies, nickles, dimes, quarters)
            if not is_made:
                print("Give more money")
            else:
                print(f"{choice_of_drink} is made")

while not stop:
    get_input()