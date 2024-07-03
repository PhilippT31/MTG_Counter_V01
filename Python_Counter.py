## MTG Counter - 02.07.2024 - P. Thorey
# The goal of this app is to have an assistant for playing magic the gathering
# The players will have a name, a lifecounter, a poison counter and a attribute which determines the playorder

## Open issues:
# -Commander Damage has not been accounted for
# -'False' is not detected if no is the input
# Some more work with strings
# 
# API implementation for the cards?
# Deck import?
# Multiple players?
# Have this one work as the counter, other source referencing this and being the main game? 

# Imports
import numpy as np
#import plotly as plt
import random

# Definiton of the players
# Playernumber, Lifecounter, Toxiccounter, First Player
player1 = np.array([1, 40, 0, 0])
player2 = np.array([2, 40, 0, 0])
player3 = np.array([3, 40, 0, 0])
player4 = np.array([4, 40, 0, 0])

# defintions
# choice_raw = {"yes": True, "y": True, "ye": True, "no": False, "n": False}

# Variables
man_inp_first = 0
state = 0
global player_stats

# Functions
def comb_players(b): #Function to combine the players arrays
    global player_stats #neccessary to determine the global array
    
    print("Log: Combination Started")    
    player_stats_1d = np.concatenate((player1, player2, player3, player4)) #appending the arrays
    print("Log: Arrays combined")
    
    player_stats_2d = player_stats_1d.reshape(4, 4) #reshaping the array to 2D
    print("Log: Array reshaped")
    print(player_stats_2d)
    
    if(b < 4):
        player_stats = np.delete(player_stats_2d, 3, 0) # this one deletes the last line of the array
        # print("Log: One line deleted")
        # print(player_stats)
        if(b == 2):
            player_stats = np.delete(player_stats, 2, 0) # this one deletes the 3rd line 
            # print("Log: One line deleted")
            # print(player_stats)
    elif(playercount == 4):
        player_stats = player_stats_2d
        
    print("Log: Array Sliced")
    print("Game array: ")
    print(player_stats)

    return(player_stats) #necessary?
    
def print_players(): #Function for fast printing of all the players (tbc)
    print("Log: Printing Players")
    print('Player 1:', player1)
    print('Player 2:', player2)
    print('Player 3:', player3)
    print('Player 4:', player4)

def define_playorder(): #Function used to define the playorder (by dice or random)
    global player_stats
    print("Log: Defining the first Player")
    
    print("Do you want to determine the starter by a dice roll?")
    choice_raw = input("Virtual (Yes) or real D20 (No)? ").lower()
    
    if(choice_raw == 'y' or 'ye' or 'yes'):
        choice = True
    elif(choice_raw == 'n' or 'no' or 'not'): #doesn't work yet
        choice = False

    if(choice == True):
        print(choice)
        p1 = random.randint(1, 20)
        p2 = random.randint(1, 20)
        p3 = random.randint(1, 20)
        p4 = random.randint(1, 20)
        p_first = np.array([p1, p2, p3, p4])
        first = np.argmax(p_first)
    elif(choice == False):
        print(choice)
        first = input("Who rolled the highest number? Player...")
        
    player_stats[first-1, -1] = 1
    print("Player", first, "is the first player")    
    print(player_stats)        

def game(): #Game with states which will follow
    global playercount
    
    state = 0
    print("Hello Players!")
    state = 1
    playercount = int(input("Enter the number of players: "))
    
    state = 2
    player_stats = comb_players(playercount)
    
    state = 3
    define_playorder()
    
    state = 20
    print("The game has finished")
    print("Final Score: ")
    print(player_stats)
    # return(state)

game() #Function call for the game