import getpass
import random
from datetime import datetime

def play():
    # list list of possible moves
    moves = ['r', 'p', 's']
    
    # User can either play against the computer or against another player
    game_mode = {1: "Single Player", 2: "2-Player" }
    
    # Timestamp for score logs
    timestamp = datetime.now()
    
    # Holds scores for each game mode
    play1_wins = 0
    play2_wins = 0
    play_ties = 0
    comp_wins = 0
    comp_ties = 0


    print("""\n
    ************************************************************
    *                                                          *
    *        Welcome to the Rock, Paper, Scissors Game!        *
    *                                                          *
    ************************************************************
    """)
    
    gameplay = True
    while gameplay:
        mode_choice = input(f"Pick a game mode!\n{game_mode} (0 to exit):  ")
        
        # match statement for game modes, 0 o exit gameplay
        match mode_choice:
            case '0':
                gameplay = False
                break
            case '1':
                try:
                    # Open Scoreboard file for 1 Player Gameplay. Will create file if one doesn't exist already.
                    scoreboard = open("/Users/tangiambe/Desktop/JUMP/Week1/Project1/rps_scores_1.txt", 'a')
                    
                    # get player1 input
                    player1  = input("[PLAYER 1] Rock(r), Paper(p), Scissors(s). Enter your choice: ").lower()

                    # user input check. Loop until user input matches choice list
                    while player1 not in moves:
                        print("INVALID INPUT: Must enter, r for Rock, p for Paper, or s for Scissors")
                        player1  = input("[PLAYER 1] Rock(r), Paper(p), Scissors(s). Enter your choice: ").lower()

                    # get computer input
                    computer  = random.choice(moves)
                    print("[COMPUTER] Rock(r), Paper(p), Scissors(s). Enter your choice: " + computer)
            
                    # Possible outcomes if Player 1 chose Rock...   
                    if player1 == "r":
                        # If Computer also chose Rock
                        if computer == "r":  
                            print("IT'S A TIE")
                            scoreboard.write("\n~Tie Game vs Computer")
                        
                        # If Computer chose Paper
                        elif computer == "p": 
                            print("COMPUTER Wins!")
                        
                        # If Computer chose Scissors
                        else: 
                            print("PLAYER 1 Wins!")
                    
                    
                    # Possible outcomes if Player 1 chose Paper...       
                    elif player1 == "p":
                        # If Computer also chose Paper
                        if computer == "p":  print("IT'S A TIE")
                        
                        # If Computer chose Scissors
                        elif computer == "s": print("COMPUTER Wins!")
                        
                        # If Computer chose Rock
                        else: print("PLAYER 1 Wins!")

                    # Possible outcomes if Player 1 chose Scissors...   
                    else:
                        # If Computer also chose Scissors
                        if computer == "s":  print("IT'S A TIE")
                        
                        # If Computer chose Rock
                        elif computer == "r": print("COMPUTER Wins!")
                        
                        # If Computer chose Paper
                        else: print("PLAYER 1 Wins!")
                    gameplay = play_again()
                    
                    # Write scores to scoreboard file
                    if gameplay == False:
                        scoreboard.write(timestamp.strftime("%b/%d/%Y %I:%M %p") + "\n")
                        scoreboard.write(f"PLAYER 1 WINS: {play1_wins}\nCOMPUTER WINS: {comp_wins}\nTIES: {comp_ties}\n\n")
                except FileNotFoundError:
                    print("File Not Found!")
                finally:
                    scoreboard.close()
                
            case '2':
                try:
                    # Open Scoreboard file for 2 Player Gameplay. Will create file if one doesn't exist already.
                    scoreboard = open("/Users/tangiambe/Desktop/JUMP/Week1/Project1/rps_scores_2.txt", 'a')
 
                    # get player1 input and HIDES it from player 2
                    player1 = getpass.getpass(prompt = "[PLAYER 1] Rock(r), Paper(p), Scissors(s). Enter your choice: ").lower()

                    # user input check. Loop until user input matches choice list
                    while player1 not in moves:
                        print("INVALID INPUT: Must enter, r for Rock, p for Paper, or s for Scissors")
                        player1  = input("[PLAYER 1] Rock(r), Paper(p), Scissors(s). Enter your choice: ").lower()

                    # get player2 input
                    player2  = input("[PLAYER 2] Rock(r), Paper(p), Scissors(s). Enter your choice: ").lower()

                    # user input check. Loop until user input matches choice list
                    while player2 not in moves:
                        print("INVALID INPUT: Must enter, r for Rock, p for Paper, or s for Scissors")
                        player2  = input("[PLAYER 2] Rock(r), Paper(p), Scissors(s). Enter your choice: ").lower()
                    
                    # Possible outcomes if Player 1 chose Rock...   
                    if player1 == "r":
                        # If Player 2 also chose Rock
                        if player2 == "r":
                            print("IT'S A TIE")
                            play_ties+=1
                        
                        # If Player 2 chose Paper
                        elif player2 == "p":
                            print("PLAYER 2 Wins!")
                            play2_wins+=1
                        
                        # If Player 2 chose Scissors
                        else:
                            print("PLAYER 1 Wins!")
                            play1_wins+=1
                    
                    
                    # Possible outcomes if Player 1 chose Paper...       
                    elif player1 == "p":
                        # If Player 2 also chose Paper
                        if player2 == "p":  
                            print("IT'S A TIE")
                            play_ties+=1
                        # If Player 2 chose Scissors
                        elif player2 == "s": 
                            print("PLAYER 2 Wins!")
                            play2_wins+=1
                        # If Player 2 chose Rock
                        else: 
                            print("PLAYER 1 Wins!")
                            play1_wins+=1

                    # Possible outcomes if Player 1 chose Scissors...   
                    else:
                        # If Player 2 also chose Scissors
                        if player2 == "s":  
                            print("IT'S A TIE")
                            play_ties+=1
                        # If Player 2 chose Rock
                        elif player2 == "r": 
                            print("PLAYER 2 Wins!")
                            play2_wins+=1
                        # If Player 2 chose Paper
                        else: 
                            print("PLAYER 1 Wins!")
                            play1_wins+=1
                    gameplay = play_again()
                    if gameplay == False:
                        scoreboard.write(timestamp.strftime("%b/%d/%Y %I:%M %p") + "\n")
                        scoreboard.write(f"PLAYER 1 WINS: {play1_wins}\nPLAYER 2 WINS: {play2_wins}\nTIES: {play_ties}\n\n")
                except FileNotFoundError:
                    print("File Not Found!")
                finally:
                    scoreboard.close()
            case _:
                print("\n~INVALID INPUT! PLEASE CHOOSE SINGLE PLAYER OR 2-PLAYER.~\n")
                

def play_again():
    '''This method is called at the end of every round of the game. 
        It asks the user if they would like to play again and returns a 
        bool based upon the user input matching possible responses in a list.
        ~ If the user inputs 'y' the method will return 'True'. 
        ~ If the user inputs 'n' the method will return 'False'. 
        ~ The method handles invalid user input and will continue to ask
        the prompt until a vaild input is given'''
    resp = ['y', 'n']
    replay = input ("Would you like to play again?\n ~ Yes (y)/ No(n) ")
    while replay not in resp:
        replay = input ("ERROR: Would you like to play again?\n ~ Yes (y)/ No(n): ")
    if replay == 'n':
        return False
    else:
        return True

