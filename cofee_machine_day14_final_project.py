MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}



def report():
    '''prints the reports of the things which are remaining'''
    print(f"water : {resources['water']}ml\n milk : {resources['milk']}ml\ncoffe : {resources['coffee']}g\nmoney : ${money}")

def processing_latte():
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    

def processing_espresso():
    resources["water"] -= 50
    resources["milk"] -= 0
    resources["coffee"] -= 18

def processing_cappuccino():
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24

def latte_insufficent():
    if resources["water"] < 200:
        print("sorry water is finished")
        return True
    elif resources["milk"] < 150:
        print("sorry milk is  finished")
        return True
    elif resources["coffee"] < 24:
        print("sorry coffe is finished")
        return True
    
def cappuccino_insufficent():
    if resources["water"] < 250:
        print("sorry water is finished")
        return True
    elif resources["milk"] < 100:
        print("sorry milk is  finished")
        return True
    elif resources["coffee"] < 24:
        print("sorry coffe is finished")
        return True
    
def espresso_insufficent():
    if resources["water"] < 50:
        print("sorry water is finished")
        return True
    elif resources["milk"] < 0:
        print("sorry milk is  finished")
        return True
    elif resources["coffee"] < 18:
        print("sorry coffe is finished")
        return True
    

        


global money
money = 0
change = 0
money_storage = 0


def coins():
    '''takes money from the user'''
    quaters = float(input("how many quaters\n"))
    dimes = float(input("how many dimes\n"))
    pennies = float(input("how many pennies\n"))
    nickels = float(input("how many nickels\n"))
    
    global money_storage
    money_storage += (quaters*0.25) + (dimes*0.10) + (pennies*0.01) + (nickels*0.05)

def money_processing():
    '''processes the money'''
    global change
    global money
    global machine_running
    global money_storage
    if which_drink == "espresso" and money_storage > 1.5:
        print("here is your espresso")
        change = money_storage - 1.5
        money += 1.5
        print(f"your change is {round(change)}")
        change = 0
        money_storage = 0
    elif which_drink == 'latte' and money_storage > 2.5:
        print("here is your latte")
        change = money_storage - 2.5
        money += 2.5
        print(f"your change is {round(change)}")
        change = 0
        money_storage = 0
    elif which_drink == "cappuccino" and money_storage > 4:
        print("here is your cappuccino")
        change = money_storage - 4
        money += 4
        print(f"your change is {round(change)}")
        change = 0
        money_storage = 0
    else:
        print("sorry not sufficient cash")
        machine_running = False 

 
machine_running = True

def coffe_machine():
    global machine_running
    while machine_running:
        global which_drink
        which_drink = input("What would you like? (espresso/latte/cappuccino)")
        if which_drink == 'espresso' and espresso_insufficent():
            espresso_insufficent()
        elif which_drink == "espresso":
            coins()
            money_processing()
            processing_espresso()
        elif which_drink == "report":
            report()
        elif which_drink == "latte" and latte_insufficent():
            latte_insufficent()
        elif which_drink == "latte":
            coins()
            money_processing()
            processing_latte()
        elif which_drink == "cappuccino" and cappuccino_insufficent():
            cappuccino_insufficent()
        elif which_drink == "cappuccino":
            coins()
            money_processing()
            processing_cappuccino()
        elif which_drink == "report":
            report()
        elif which_drink == "off":
            machine_running = False

coffe_machine()
        

