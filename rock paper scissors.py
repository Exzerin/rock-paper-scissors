import random 

# this is a mess lol I'll come back to this

choices = ['ROCK', 'PAPER', 'SCISSORS']

def rock_paper_scissors():
    
    pc_choice = random.choice(choices)

    user_choice = input('Choose ROCK, PAPER, or SCISSORS: ').upper()
    
    print('Rock, paper, scissors shoot!')
    
    if user_choice == 'ROCK':
        if pc_choice == 'ROCK':
            print("It's a tie! The pc chose", pc_choice, '.')
            
        elif pc_choice == 'PAPER':
            print('You lose! The pc chose', pc_choice, '.')
            
        else:
            print('You win! The pc chose', pc_choice ,'.')
            
            
    if user_choice == 'PAPER':
        if pc_choice == 'PAPER':
            print("It's a tie! The pc chose", pc_choice, '.')
            
        elif pc_choice == 'SCISSORS':
            print('You lose! The pc chose', pc_choice, '.')
            
        else:
            print('You win! The pc chose', pc_choice ,'.')           
            
                
    if user_choice == 'SCISSORS':
        if pc_choice == 'SCISSORS':
            print("It's a tie! The pc chose", pc_choice, '.')
            
        elif pc_choice == 'ROCK':
            print('You lose! The pc chose', pc_choice, '.')
            
        else:
            print('You win! The pc chose', pc_choice ,'.')           
            
rock_paper_scissors()
