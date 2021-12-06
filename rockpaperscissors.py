import random

user = input("Pick one: rock, paper, scissors! ")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

print(f"\n You chose {user}, computer chose {computer}.\n")
