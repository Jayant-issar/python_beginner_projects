print('welcome to treasure your misson is to find the treasure')
l_or_r = input("you have came to a dead end now ....... where do you wanna go, type R for right and L for left")
if l_or_r == "R":
    print("opppsssssssss....... that was a big valley out there you died.")
else:
    river = input("there you go with your wise decision you have come to river what will you do SWIM or WAIT for the boat to come")
    if river == "SWIM":
        print("you were attacket by pirans you died cause you swimed")
    else:
        door = input("you have reached the last stage of the game .... there are three doors which doors you wanna take? BLUE,RED or GREEN?")
        if door == "RED":
            print('OHHHHHHH NOOOOOOOO..........you were burned by fire and the game is over')
        elif door == "BLUE":
            print("OHHHHH NOOOOOOO........YOU WERE EATEN BY BEAST ITS OVER FOR YOU")
        elif door == "GREEN":
            print("CONGRATULATIONSSSSSSSSSS......you have reached the safe green fileds and now you are safe..")
        else:
            print("not any thing from the options you wasted your time and now being chased by wild anacondas its a game over for you ")



