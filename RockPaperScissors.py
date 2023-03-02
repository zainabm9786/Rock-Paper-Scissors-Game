#RockpaperScissors

import random
def play():
    user= input("Select 'r' for rock, 'p' for paper, or 's' for scissors: ")
    computer=random.choice(['r','p','s'])
    print(computer)
    if user==computer:
        return "It's a tie!"
    
    #r>s, s>p, p>r
    if is_win(user,computer):
        return 'You won!'
    
    return 'You Lost!'

def is_win(player, opponent):
    #return true is player wins
    if (player=="r" and opponent=='s') or (player=="s" and opponent=='p') \
        or (player=='p' and opponent=='r'):
        return True

print(play())