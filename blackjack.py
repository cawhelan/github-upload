import random
import os
import time

# different suits
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# hold image of suit as value
suitsVal = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

# type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# value attached to card (ace starts high)
cardsVal = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# quit message
quitGame = "Okay fine, suit yourself!"

print("Welcome to blackjack you trying to gamble?")
print("1. Hell yeah")
print("2. Nah I'm weak")
choice = input()


if choice == "1":

elif choice == "2":
    print(quitGame)
