import random 
import math 

def play():
    
    user = input("ROCK, PAPER, or SCISSORS?\n")
    user = user.upper()
    
    computer = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
    
    if user == computer:
        return (0, user, computer)
    
    if is_win(user, computer):
        return (1, user, computer)
    
    return (-1, user, computer)

def is_win(player, opponent):
    # return true if the paper beats the opponnent 
    # winning conditions rock > scissors, scissors > paper, paper > rock
    if (player == "ROCK" and opponent == "SCISSORS") or (player == "SCISSORS" and opponent == "PAPER") or (player == "PAPER" and opponent == "ROCK"):
        return True
    return False 

def play_best_of(n):
    # play agaisnt pc until someone wins best of n games
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie 
        if result == 0:
            print('It is a tie. You both chose {}.\n'.format(user))
        # win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost..\n'.format(user, computer))
        
    if player_wins > computer_wins:
        print('You won best of {} games! Good job'.format(n))
    else:
        print:('The computer has won best out of {} games. Try again later.'.format(n))
        
if __name__ == '__main__':
    play_best_of(3)
