#rock paper scissor

import random

options=["rock","paper","scissors"]
points=5


def winner(player_choice,computer_choice,points):
    if player_choice == computer_choice:
        print("it's a tie")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")):
        outcome="player wins"
        points-=1
        print("player wins!")
        score(outcome)
    else:
        outcome="computer wins"
        points-=1
        print( "Computer wins!")
        score(outcome)


def score(outcome):
    if outcome=="player wins":
        player_score+=1
    else:
        computer_score+=1
    print("Score: Player -",player_score,"| Computer -",computer_score)
        
def game():
    print("ROCK PAPER SCISSORS")
    print("-------------------")
    print("let's play")
    player_score, computer_score=0,0
    
    while (points>0):
        #choices
        player_choice=input("Pick one (rock , paper , scissors)").lower()
        
        if player_choice not in options:
            player_choice=input("invalid choice, try again!").lower()
            
        computer_choice= random.choice(options)
        
        print("Player chose:",player_choice," | ","Computer chose:",computer_choice)
        print(winner(player_choice,computer_choice,points))
               
game()
