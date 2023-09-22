
from ART import logo,vs
from data_day13_higher_lower import data
import random

print(logo)
print("welcome to higher lower game")

def option_a():
    global choice_a
    choice_a = random.choice(data)
    return choice_a

def option_b():
    global choice_b
    choice_b = random.choice(data)
    return choice_b

def comparision():
    global user_choice
    user_choice = input("what is your answer press a for option a and b for option b\n")
    if user_choice == 'a':
        user_choice = choice_a
    else:
        user_choice = choice_b
    
    
    global game_running
    global correct_option
    correct_option = choice_a
    if int(choice_a['follower_count']) > int(choice_b['follower_count']):
        correct_option = choice_a
    else:
        correct_option = choice_b
        
    
    if user_choice == correct_option:
        global score
        score = 0
        print("correct answer")
        score = score + 1
    else:
        print(f"wrong answer your score is {score}")
        game_running = False


game_running = True

def game():
    while game_running:
        option_a()
        A = f"{choice_a['name']}, a {choice_a['description']}, from the {choice_a['country']}"
        print(A)
        print(vs)
        option_b()
        B = f"{choice_b['name']}, a {choice_b['description']}, from the {choice_b['country']}"
        print(B)
        
        comparision()

game()




        


