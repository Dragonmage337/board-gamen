"MAIN"
import time
import random



"""Random Number Game"""

def StartGame():
    x = input("Hello there, Users! Would you like to play a game?")
    if x == 'y' or x == 'yes':
        Main()
    elif x.lower == 'n' or x.lower == 'no':
        print("Ok, I guess.")
        time.sleep(10)
        StartGame()

def Main():
    print("Player 1, roll the 'dice'")
    xa = input("Roll?")
    if xa.lower == 'y' or xa.lower == "yes":
        p1 = random.randint(1,100)
        print("Ok, next it is Player 2's turn")
    xb = input("Roll?")
    if xb.lower == 'y' or xb.lower == "yes":
        p2 = random.randint(1,100)
        print("Alright Both players have rolled!")
StartGame()