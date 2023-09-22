import random
print("welcome to number guessing game\n I'am thinking of a number between 1 and 100")
difficulty_level = input("choose a difficulty level type easy or hard as per your choice\n").lower()


hard_lives = 5
def hard_attempts():
    '''deals with the lives when difficulty is hard'''
    global hard_lives
    hard_lives = hard_lives - 1
    return hard_lives

easy_lives = 10
def easy_attempts():
    '''deals with lives when difficulty is easy'''
    global easy_lives
    easy_lives -= 1
    return easy_lives

answer = random.randint(1,100)

game_running = True

def guess():
    '''takes user input for the guess'''
    global game_running
    global guessed_number
    guessed_number = int(input("make a guess\n"))
    if guessed_number == answer:
        print("you won the game")
        game_running = False
    else:
        print("try again")
        game_running

def lives_over_hard():
    '''checks for the lives in hard diificulty mode and ends the game (game_running while loop) if hard_lives is 0'''
    global game_running
    if hard_lives == 0:
        print(f"ohoho no you ran out of lives the answer was {answer} and you lost")
        game_running = False


def lives_over_easy():
    '''checks for the lives in easy diificulty mode and ends the game (game_running while loop) if hard_lives is 0'''
    global game_running
    if easy_lives == 0:
        print(f"ohoho no you ran out of lives the answer was {answer} and you lost")
        game_running = False        

def high_low():
    '''checks for the answers and tells if the guessed answer is too high or too low'''
    global guessed_number
    if guessed_number > answer:
        print("too high\n")
    elif guessed_number < answer:
        print("too low\n")                

if difficulty_level == 'hard':
    while game_running:
        print(f"you have {hard_lives} attempt left")
        hard_attempts()
        guess()
        high_low()
        lives_over_hard()
elif difficulty_level == 'easy':
    while game_running:
        print(f'you have {easy_lives} attmpts left')
        easy_attempts()
        guess()
        high_low()
        lives_over_easy()
else:
    print("invalid input")






