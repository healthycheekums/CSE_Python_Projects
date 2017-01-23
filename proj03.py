##############################################################################  
#  Computer Project #3  
#    
#  Algorithm  
#     Print introduction  
#     Prompts for user inputs 
#     Establishment of constants and importing of random library 
#     For loop of if statements to determine the outputs and output count         
#     Calculation of percentiles needed for outputs 
#         Display of indicated outputs of distrobution 
##############################################################################  

#This is the introductory statement 
print ( """Welcome to Rock-Paper-Scissors\n\
Enter a single character: 'r', 's', 'p', or 'q' to quit.\n\
Rock Beats Scissors which beats Paper which beats Rock.""") 

import random 
random.seed( 0 ) 
ROCK = 1
PAPER = 2
SCISSORS = 3
PERCENT = 100
computer_throw = 0
tie_count, user_wins, computer_wins = 0,0,0
rock_throws, scissors_throws, paper_throws,total_throws = 0,0,0,0

while True:
    throw = input('enter a command (rspq) ')
    computer_throw = random.randint(1,3)
    if throw == 'r':
        throw = ROCK
        if  throw == computer_throw:
            print('User chose r and com chose r \nThis round is a tie')
            tie_count  += 1
        if SCISSORS == computer_throw:
            print('User chose r and computer chose s \nUser wins this round')
            user_wins +=1
        if PAPER == computer_throw:
            print('User chose r and computer chose p \nCom wins this round')
            computer_wins +=1
        rock_throws +=1
        continue
    
    if throw == 's':
        throw = SCISSORS
        if  throw == computer_throw:
            print('User chose s and computer chose s \nThis round is a tie')
            tie_count  += 1
        if PAPER == computer_throw:
            print('User chose r and computer chose p \nUser wins this round')
            user_wins +=1
        if ROCK == computer_throw:
            print('User chose r and computer chose r \nCom wins this round')
            computer_wins +=1
        scissors_throws +=1
        continue
        
    if throw == 'p':
        throw = PAPER
        if  throw == computer_throw:
            print('User chose p and computer chose p \nThis round is a tie')
            tie_count  += 1
        if  computer_throw < throw:
            print('User chose p and computer chose s \nUser wins this round')
            user_wins +=1
        if throw < computer_throw:
            print('User chose p and computer chose r \nCom wins this round')
            computer_wins +=1
        paper_throws +=1
        continue
    total_throws = rock_throws + scissors_throws + paper_throws
    user_win_per = user_wins/total_throws*PERCENT
    com_win_per = computer_wins/total_throws*PERCENT
    tie_per = tie_count/total_throws*PERCENT
    rock_per = rock_throws/total_throws*PERCENT
    scissor_per = scissors_throws/total_throws*PERCENT
    paper_per = paper_throws/total_throws*PERCENT            
    if throw == 'q':
        break
    
    else:
        print('Please enter a valid command')
        continue

print('Summary Statistics \n\tUser wins:',user_wins,'(',round(user_win_per,1)\
,'%)\n\tComputer wins:',computer_wins,'(',round(com_win_per,1)\
,'%)\n\tTies:',tie_count,'(',round(tie_per,1),'%)')

print('User Statistics \n\tRock:',rock_throws,'(',round(rock_per,1),'%)\n\t\
Paper:',paper_throws,'(',round(paper_per,1),'%)\n\tScissors:',scissors_throws\
,'(',round(scissor_per,1),'%)')