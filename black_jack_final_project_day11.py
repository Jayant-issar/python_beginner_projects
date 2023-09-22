############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


print("welcome to black jack game")
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
user_card = []
pc_card = []
pseudo_pc_card = []


def card_distribution():
    for i in range(2):
        user_card.append(random.choice(cards))
        pc_card.append(random.choice(cards))

def pseudo_card_fun():
    for n in pc_card:
        pseudo_pc_card.append(n)
    pseudo_pc_card[random.randint(0,len(pseudo_pc_card)-1)] = 'X'


def sum_user():
    global user_sum
    user_sum = 0
    for n in user_card:
        user_sum = n + user_sum
    

def sum_pc():
    global pc_sum
    pc_sum = 0
    for n in pc_card:
        pc_sum = n + pc_sum 
    


def the_game():
    print(f'your cards are = {user_card}')
    print(f"computer's cards are = {pseudo_pc_card}")
    hit_stand = input("what do you want to do hit or stand \n").lower()
    
    if hit_stand == 'stand':
        sum_user()
        sum_pc()
        if pc_sum < 17:
            while pc_sum >= 17:
                pc_card.append(random.choice(cards))
        if pc_sum and user_sum > 21:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("its a draw")
        elif user_sum and pc_sum == 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("Its a draw homie")
        elif user_sum == 21:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("you won the game and pc lost")    
        elif pc_sum == 21:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("you lost the game and pc won") 
        elif pc_sum > 21:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("you won the game and pc lost")
        elif user_sum > 21:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("you lost the game and pc won")
        elif pc_sum > user_sum:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("pc won the game and you lost")
        elif user_sum > pc_sum:
            print(f"your cards are {user_card}")
            print(f"pc cards are {pc_card}")
            print("you won the game and pc lost")
    else:
        if hit_stand == "hit":
            user_card.append(random.choice(cards))
            sum_user()
            sum_pc()
            if pc_sum < 17:
                while pc_sum >= 17:
                    pc_card.append(random.choice(cards))
            sum_pc()        
            if pc_sum and user_sum > 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("its a draw")
            elif user_sum and pc_sum == 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("Its a draw homie")
            elif user_sum == 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("you won the game and pc lost")    
            elif pc_sum == 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("you lost the game and pc won")    
            elif pc_sum > 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("you won the game and pc lost")
            elif user_sum > 21:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("you lost the game and pc won")    
            elif pc_sum > user_sum:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("pc won the game and you lost")
            elif user_sum > pc_sum:
                print(f"your cards are {user_card}")
                print(f"pc cards are {pc_card}")
                print("you won the game and pc lost")
        else:
                print("invalid input")



card_distribution()
sum_pc()
sum_user()
pseudo_card_fun()

the_game()






