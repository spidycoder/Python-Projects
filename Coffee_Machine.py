from secrets import choice


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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficietn(order_ingredients):
    '''Return True when order can be made,false when order can't be made'''
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry,there is not enough {item} ")
            return False
    return True


def process_coins():
    '''Return the total money collected form the user'''
    print("Enter the money: ")
    total=int(input("Enter the quarters "))*0.25
    total+=int(input("Enter the dimes "))*0.1
    total+=int(input("Enter the nickles "))*0.05
    total+=int(input("Enter the pennies "))*0.01
    return total


def is_payment_successful(money_collected,drink_cost):
    '''Return True if payment is accepted otherwise False'''
    if money_collected<drink_cost:
        print("Sorry,insufficient Money,money refunded")
        return False
    else:
        change = round(money_collected-drink_cost,2)
        print(f"Here is the change of ${change}")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your ☕{drink_name} drink")


is_on=True
while is_on:
    choice=input("What would you like to drink:(espresso,latte,cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}ml")
        print(f"money:${profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficietn(drink["ingredients"]):
            payment=process_coins()
            if is_payment_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])



