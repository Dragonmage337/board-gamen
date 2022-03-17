"MAIN"
import time
import random
from tkinter import Place



"""Random Number Game"""

PLAYER1 = {
    "Marbles" : 5
}

PLAYER2 = {
    "Marbles2" : 5
}

def StartGame():
    x = input("Hello there, Users! Would you like to play a game?")
    if x == 'y' or x == 'yes':
        Main()
    elif x == 'n' or x == 'no':
        print("Ok, I guess.")
        time.sleep(10)
        StartGame()

def Main():
    print("Player 1, roll the 'dice'")
    xa = input("Roll?")
    if xa == 'y' or xa == "yes":
        p1 = random.randint(1,100)
        print("Ok, next it is Player 2's turn")
    xb = input("Roll?")
    if xb == 'y' or xb == "yes":
        p2 = random.randint(1,100)
        print("Alright both players have rolled!")


def Decision():
    print("Now to get to the interesting part!")
    time.sleep(1)
    print("BETTING HAHAHHAHAHHAHAH!!!!!")
    ya = input("Hey...Player1, do you wanna bet the marbles you have? Btw you start off with 5.")
    if ya == 'yes' or ya == 'y':
        bet = random.randint(1,5)
        PLAYER1 ["Marbles"] = PLAYER1 ["Marbles"]


    
StartGame()