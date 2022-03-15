"MAIN"
import time
import random



"""Random Number Game"""

def StartGame():
    x = input("Hello there, User! Would you like to play a game?")
    if x.lower == 'y' or x.lower == 'yes':
        Main()
    elif x.lower == 'n' or x.lower == 'no':
        print("Ok, I guess.")
        time.sleep(10)
        StartGame()

def Main():
    print("Player 1, roll the 'dice'")
    x = input("Roll?")
    if x 