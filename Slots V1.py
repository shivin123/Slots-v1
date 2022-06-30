#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Set to 1 for extra info for debugging 
debug_mode=0
#imports 
import random 
from IPython.display import clear_output

#mem arrays
d_board=[[0 for i in range(3)]for e in range(3)]
money=100
sym=[0,1,2,3,4]
symbols=["¶","¤","§","Æ","ß"]


def pick_sy(d_board):
    for i in range(3):
        for e in range(3):
            d_board[i][e]=random.choice(sym)
        

def print_board(d_board):
    for i in d_board:
        temp=" "
        for e in i:
            temp=temp+symbols[e]+" "
        print(temp)
        
        
def check_win(d_board):
    w=[-1,-1,-1]
    
    for i in range(3):
        if debug_mode==1:
            print(set(d_board[i]))
        if len(set(d_board[i]))==1:
            w[i]=d_board[i][0]
    if debug_mode==1:
        print(w)
    return w
    
if debug_mode==1:
    pick_sy(d_board)
    print_board(d_board)
    check_win(d_board)
    
while money>0:
    clear_output(wait=True)
    input("Hit enter to pull the lever")
    money-=3
    pick_sy(d_board)
    print_board(d_board)
    winnings=check_win(d_board)
    for i in winnings:
        if i!=-1:
            winning=2*((i+1)**2)
            money+=winning
            print("You win:")
            print(str(winning))
            
    print("money:"+str(money))
    
print("You have run out of money the bouncer has kicked you out.")

