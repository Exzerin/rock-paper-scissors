import random 
import math 

def play():
    
    user = input("ROCK, PAPER, or SCISSORS?\n")
    user = user.upper()
    
    computer = random.choice(["ROCK", "PAPER", "SCISSORS"])
    
    if user == computer:
        return "You and the computer both chosed {}. It's a tie.".format(computer)
    
    if is_win(user, computer):
        return "You chose {} and the computer chose {}. You won!".format(user, computer)
    
    return "You chose {} and the computer chose {}. You lose!".format(user, computer)

def is_win(player, opponnent):
    # return true if the paper beats the opponnent 
    # winning conditions rock > scissors, scissors > paper, paper > rock
    if (player == "ROCK" and opponnent == "SCISSORS") or (player == "SCISSORS" and opponent == "PAPER") or (player == "PAPER" and opponnent == "ROCK"):
        return True
    return False 

def play_best_of(n):
    # play agaisnt pc until someone wins best of n games
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        
    
if __name__ == '__main__':
    print(play())    
    print(play_best_of(5))
