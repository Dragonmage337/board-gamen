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
    
    if x == "y" or x == "yes":
        Main()
    elif x == 'n' or x == 'no':
        print("Ok, I guess.")
        time.sleep(10)
        StartGame()
p1 = random.randint(1,100)
p2 = random.randint(1,100)
def Main():
    print("Player 1, roll the 'dice'")
    xa = input("Roll?")
    if xa == 'y' or xa == "yes":
        
        print("Ok, next it is Player 2's turn")
    xb = input("Roll?")
    if xb == 'y' or xb == "yes":
        
        print("Alright both players have rolled!")
        DecisionA()

bet = random.randint(1,5)

def DecisionA():
    print("Now to get to the interesting part!")
    time.sleep(1)
    print("BETTING HAHAHHAHAHHAHAH!!!!!")
    ya = input("Hey...Player1, do you wanna bet the marbles you have? Btw you start off with 5.")
    if ya == 'yes' or ya == 'y':
        PLAYER1 ["Marbles"] = PLAYER1 ["Marbles" ] - bet
        print("Alright, you roll the die and put up ", PLAYER1 ["Marbles"])
        DescisionB()
    if ya == 'no' or ya == 'n':
        print("Alright well since you don't want to bet, let's reveal the numbers")
        time.sleep(1)
        print("Player 2, since Player 1 didn't bet, you can't either!")
        Results()
def DescisionB():
    print("Alright, now it is your turn Player 2!")
    time.sleep(1)
    l = input("Do you want to bet?")
    if l.lower == 'yes' or l.lower == 'y':
        print("Alright we have a fun game going!")
        PLAYER2 ["Marbles2"] = PLAYER2 ["Marbles2"] - bet
        print("Alright, you roll the die and put up ", PLAYER2 ["Marbles2"])
        Results()
    else:
        print("Well since Player 2 didn't bet, no one bets!")
        PLAYER1 ["Marbles"] = PLAYER1 ["Marbles"] + bet
        print(PLAYER1 ["Marbles"])
        print([PLAYER2 ["Marbles2"]])
        print("No one will lose anything!")
        Results()




def Results():
    print("Alright here are the final results!")
    print("Player 1 : ",p1)
    print("Player 2 : ",p2)
    if p1 < p2:
        print("Player 1, you win!")
        StartGame()
    elif p1 == p2:
        print("Its a tie!")
        StartGame()
    else:
        print("Player 2 wins!")
        StartGame()


    
StartGame()