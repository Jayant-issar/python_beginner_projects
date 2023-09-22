import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
RPS = ['0','1','2']

computer_choice = RPS[random.randint(0,2)]

human_choice = input('What do you choose, press 0 for rock 1 for papper and 2 for scissors...')

if human_choice == '0':
    print(rock)
elif human_choice == '1':
    print(paper)
elif human_choice == '2':
    print(scissors)
else:
    print("wrong option you lost due to breaking the rules")

print('COMPUTER CHOOSES:....')

if computer_choice == '0':
    print(rock)
elif computer_choice == '1':
    print(paper)
elif computer_choice == '2':
    print(scissors)
else:
    print('computer dont want to play with you get lost')

won = 'CONGRATULATION YOU WON'
draw = 'ITS A DRAW'
lost = 'ohhhhhhh nooo YOU LOST........'

if human_choice == '0' and computer_choice == '0':
    print(draw)
elif human_choice == '0' and computer_choice == '1':
    print(won)
elif human_choice =='0' and computer_choice == '2':
    print(lost)
elif human_choice == '1' and computer_choice == '0':
    print('won')
elif human_choice == '1' and computer_choice == '1':
    print(draw)
elif human_choice == '1' and computer_choice == '2':
    print(lost)
elif human_choice == '2' and computer_choice == '0':
    print(lost)
elif human_choice == '2' and computer_choice == '1':
    print(won)
elif human_choice == '2' and computer_choice == '2':
    print(draw)
else:
    print('sorry the game just crashed')

    



    

