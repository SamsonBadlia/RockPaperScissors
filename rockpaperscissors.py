import random

user = input("Pick one: rock, paper, scissors! ")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

print(f"\n You chose {user}, computer chose {computer}.\n")

def printWinPhrase():
    print(f"{user} beats {computer} which means you win")

def printLossPhrase():
    print(f"{computer} beats {user} which means you dead lost to the computer bro")

def printTiePhrase():
    print(f"Both yall selected {user}. It's a tie!")

if user == computer: printTiePhrase()
elif user == "rock":
    if computer == "scissors": printWinPhrase()
    else: printLossPhrase()
elif user == "paper":
    if computer == "rock": printWinPhrase()
    else: printLossPhrase()
elif user == "scissors":
    if computer == "paper": printWinPhrase()
    else: printLossPhrase()
