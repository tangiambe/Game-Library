''' game menu, when game is selected, import file/module of that game, that's where all the methods are
# have one .play() method from each module when game is selected
#ex: 
# Which Game Would You Like To Play?
# 1. RPS
# User enters 1
# import rps module & call rps.play() in this file

 This is the main file. Run this file to select and play a particular
    game.'''

import rps
import sys


game_lib = {
    1: "Rock-Paper-Scissors",
    2: "Number Guess", #not implemented yet
    3: "Tic-Tac-Toe", #not implemented yet
}



while True:
    print(f"\nLet's Play a Game!\n\n{game_lib}")
    game_choice = input("\nPick a game to play! (0 to Log Out): ")
    
    match game_choice:
        case '0':
            print("Bye Bye!")
            sys.exit()
        case '1':
            rps.play()
            userIn = input("\nEnter any key to return to Menu. (0 to Log Out): ")
            if userIn == '0':
                print("Bye Bye!")
                sys.exit()
            else: 
                continue  
        case _:
            print("~INVALID INPUT! PLEASE ENTER THE GAME ID.~\n")
            
        
