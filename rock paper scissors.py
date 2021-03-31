import random 

def play():
    
    user = input("ROCK, PAPER, or SCISSORS?").upper()
    
    computer = random.choice(["ROCK", "PAPER", "SCISSORS"])
    
    if user == computer:
        return "You and the computer both chosed {}. It's a tie.".format(computer)
    
    if is_win:
        return "You chose {} and the computer chose {}. You won!".format(user, computer)
    
    return "You chose {} and the computer chose {}. You lose!".format(user, computer)

def is_win(player, opponent):
    # return true if the paper beats the opponnent 
    # winning conditions rock > scissors, scissors > paper, paper > rock
    if (player == "ROCK" and opponnent == "SCISSORS") or (player == "SCISSORS" and opponent == "PAPER") or (player == "PAPER" and opponnent == "ROCK"):
        return True
    return False 
    
if __name__ == '__main__':
    print(play())    
