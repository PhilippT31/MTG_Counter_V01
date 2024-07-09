## MTG Counter - 02.07.2024 - P. Thorey
# The goal of this app is to have an assistant for playing magic the gathering
# The players will have a name, a lifecounter, a poison counter and a attribute which determines the playorder

# What happens during the game?
# -Deciding how many players are there (x)
# -Deciding who is the starting player (x)
# -Counting the life
# -Indicating who's turn it is
# -Deciding when the game is over
# -One player leaving the game

## Open issues:
# -Commander Damage has not been accounted for
# -'False' is not detected if no is the input
# -Some more work with strings
# -Inputs out of range need to be detected, and a replacement is needed
# -Saving the stats if a player loses for scoreboard
# -Counter for the playrounds
# -The input for the randomizerdoesn't work? Doesn't accept letters nor numbers (tempfix)

## Further Ideas
# API implementation for the cards?
# Deck import?
# Multiple players?
# Have this one work as the counter, other source referencing this and being the main game? 

# Imports
import numpy as np
import random
#import plotly as plt

# Definiton of the players
# Playernumber, Lifecounter, Toxiccounter, First Player
player1 = np.array([1, 40, 0, 0])
player2 = np.array([2, 40, 0, 0])
player3 = np.array([3, 40, 0, 0])
player4 = np.array([4, 40, 0, 0])

# defintions
# choice = {"yes": True, "y": True, "ye": True, "no": False, "n": False}

# Variables
man_inp_first = 0
state = 0
global player_stats
logging = True
choice = False
active_player = 1
turncounter = 0

# Functions
def logprint(text):
    if(logging == True):
        print(text)

def comb_players(b): #Function to combine the players arrays
    global player_stats #neccessary to determine the global array
    
    logprint("Log: Combination Started")    
    player_stats_1d = np.concatenate((player1, player2, player3, player4)) #appending the arrays
    logprint("Log: Arrays combined")
    
    player_stats_2d = player_stats_1d.reshape(4, 4) #reshaping the array to 2D
    logprint("Log: Array reshaped")
    logprint(player_stats_2d)
    
    if(b > 4):
        print("Input invalid: Out of range (Too High)")
        parsing = input("Parse to 4? [y/n] ").lower()
        if(parsing == "y"):
            b = 4
            print(b, "players are playing")
        elif(parsing == "n"):
            b = int(input("Enter the number of players: "))
    elif(b < 2):
        print("Input invalid: Out of range (Too Low)")
        parsing = input("Parse to 4? [y/n] ").lower()
        if(parsing == "y"):
            b = 2
        elif(parsing == "n"):
            b = int(input("Enter the number of players: "))
            print(b, "players are playing")
                    
    if(b < 4):
        player_stats = np.delete(player_stats_2d, 3, 0) # this one deletes the 4th line
        # print("Log: One line deleted")
        # print(player_stats)
        if(b == 2):
            player_stats = np.delete(player_stats, 2, 0) # this one deletes the 3rd line 
            # print("Log: One line deleted")
            # print(player_stats)
    else:
        player_stats = player_stats_2d
        
    logprint("Log: Array Sliced")
    logprint("Game array: ")
    logprint(player_stats)

    return(player_stats) #necessary?
    
# def print_players(): #Function for fast printing of all the players (tbc)
# this function should also save the playstats, as well as order them and input the newest stats
# input state? Therefore diffrerent print modes could be used (end, current state)
    # print("Log: Printing Players")
    # print('Player 1:', player1)
    # print('Player 2:', player2)
    # print('Player 3:', player3)
    # print('Player 4:', player4)

def define_playorder(players): #Function used to define the playorder (by dice or random)
    global player_stats
    global active_player
    logprint("Log: Playorder() started")
    
    skip = True
    if(skip == False):
        print("Do you want to determine the starter by a dice roll?")
        choice_raw = 'a'
        choice_raw = input("Virtual (Yes) or real D20 (No)? [y/n] ").lower() #No input is accepted 
    elif(skip == True):
        choice_raw = 'y'
    logprint("Log: Input was given")
    
    if(choice_raw == 'y'):
        choice = True
    elif(choice_raw == 'n'): 
        choice = False
    else:
        print("No valid answer was given, the starting player is decided by a random dice roll.")
        choice = True
        
    logprint(choice)
    
    if(choice == True):
        p1 = random.randint(1, 20)
        p2 = random.randint(1, 20)
        p3 = random.randint(1, 20)
        p4 = random.randint(1, 20)
        p_first = np.array([p1, p2, p3, p4])
        first = np.argmax(p_first)
        if(first >= players):
            first = players
    elif(choice == False):
        first = int(input("Who rolled the highest number? Player..."))
    logprint(first)
    player_stats[first, -1] = 1
    print("Player", first+1, "is the first player")    
    logprint(player_stats)        
    
def nextplayer(): #runnning through the different players
    global active_player #indexing the row of player_stats of the active player
    logprint("Active Player: ")
    logprint(active_player)
    active_player + 1
    if(active_player > 3):
        active_player = 0
    turn()
    
def player_lost(player):
    
    if(player_stats[player-1, 1] <= 0):
        print("Player", player, "is leaving the game.")
    

def game_start():
    global active_player
    print("The game has started!")
    print("It's player ", active_player, "'s turn.")
    
def turn():
    global turncounter
    
    damage
    damage_cmd
    damage_tox
    
    nextplayer()

def game(): #Game with states which will follow
    state = 0
    print("Hello Players!")
    
    state = 1
    playernumber = int(input("Enter the number of players: "))
    player_stats = comb_players(playernumber)
    
    state = 2
    define_playorder(playernumber)
    
    state = 3
    game_start()
    
    state = 4
    turn()
    
    state = 10
    
    state = 20
    print("The game has finished")
    print("Final Score: ")
    print(player_stats)
    # return(state)

game() #Function call for the game