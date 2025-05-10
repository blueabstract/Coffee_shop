from random import choice
from art import logo,symbol

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
money=0

def check_availability(rsc):
    if resources["water"]>= MENU[rsc]["ingredients"]["water"] and resources["coffee"]>=MENU[rsc]["ingredients"]["coffee"] and resources["milk"]>=MENU[rsc]["ingredients"]["milk"] :
        return True
    else:
        return False

def calculate_money(q,d,n,p):
    q_converted=q*0.25
    d_converted=d*0.10
    n_converted = n * 0.05
    p_converted = p * 0.01
    total=q_converted+d_converted+n_converted+p_converted
    return total

def check_transaction(total,chc):
    global money
    if total==MENU[chc]["cost"]:
        money+=MENU[chc]["cost"]
        return True

    elif total>MENU[chc]["cost"]:
        change=round(total-MENU[chc]["cost"],2)
        money += MENU[chc]["cost"]

        print(f"Here is ${change} in change ")
        return True


    else:
        print("Sorry That's Not Enough Money! Money Refunded....")
        return False

def make_coffee(chc):
    global resources
    resources["water"]-=MENU[chc]["ingredients"]["water"]
    resources["milk"] -= MENU[chc]["ingredients"]["milk"]
    resources["coffee"] -= MENU[chc]["ingredients"]["coffee"]
    print(f"Here is your {chc}! Enjoy!")





is_running = True

while is_running:
    print(symbol)
    choice=input("What Would You Like?(espresso/latte/cappuccino)").lower()

    if choice=="report":
        print(f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Profit: {money}""")


    elif choice=="off":
        print("THANK YOU FOR VISITING!!!")
        break


    elif choice in ("espresso","latte","cappuccino"):
        if check_availability(choice):
            print("Please Insert Coins:")
            quarter=int(input("How many quarters?"))
            dime=int(input("How many dimes?"))
            nickel=int(input("How many nickels?"))
            penny=int(input("How many pennies?"))
            total_money=calculate_money(quarter,dime,nickel,penny)
            if check_transaction(total_money,choice):
                make_coffee(choice)

        else:
            print(f"Sorry! {choice} is not available right now...")

    else:
        print("Incorrect Choice!! Enter Again!")






