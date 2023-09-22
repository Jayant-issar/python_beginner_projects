logo = """ _____________________
|  _________________  |
| |  jayant's calc  | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def substraction(n1, n2):
    return n1-n2   

operator_dict = {
                "+":add,
                "-":substraction,
                "*":multiply,
                "/":divide
                 }
calculation_going_on  =True
num1 = int(input("what is the first number?"))

while calculation_going_on:
    
    num2 = int(input("what is the second number?"))

    for n in operator_dict:
        print(n)

    which_operation = input("pick a operator from above")

    main_calculator = operator_dict[which_operation]

    answer = main_calculator(num1, num1)

    resume = input(f"your answer is {answer} do you want to continue with {answer} as your first number..yes or no?")

    if resume == 'yes':
        calculation_going_on
        num1 = answer
    else:
        calculation_going_on = False

