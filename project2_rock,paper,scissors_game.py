#This is the classic Rock, Paper and Scissors Game:

import random

print("===========Welcome to the GAME==============")
#Dictionary for the computer program to run
computer_dict = {'rock' : -1, 'paper' : 0, 'scissors': 1}

#Dictionary for conversion of the player input to computer program language
player_dict = { -1 : 'rock' , 0 : 'paper', 1 : 'scissors'}
while(True):
    try:
         
         #Here computer will chose randomly
        computer_choice = random.choice([-1,0,1])

        #Input from the player
        player_input = input("Enter your choice : ")

        #if player input any other value than the required ones
        if player_input not in computer_dict:
            print("Invalid Input!!Please try again")
            continue
        
        #Converting user's string input into integer for the program
        player_choice = computer_dict[player_input]

        print(f"You chose : {player_input} and computer chose : {player_dict[computer_choice]}")

        if computer_choice == -1 and player_choice == -1:      
            print("Game tied!!!!")

        elif computer_choice == -1 and player_choice == 0:
            print("You Won!!")

        elif computer_choice == -1 and player_choice == 1:
            print("You Lost!!!!")

        elif computer_choice == 0 and player_choice == -1:
            print("You Lost!!!!")

        elif computer_choice == 0 and player_choice == 0:
            print("Game Tied!!!!")

        elif computer_choice == 0 and player_choice == 1:
            print("You Won!!!!")

        elif computer_choice == 1 and player_choice == -1:
            print("You Won!!!!")

        elif computer_choice == 1 and player_choice == 0:
            print("You Lost!!!!")

        elif computer_choice == 1 and player_choice == 1:
            print("Game Tied!!!!")

    except ValueError:
        print("Invalid Input!! Please put a valid input")

    continue_game = input("Do you want to continue?(Yes/No) : ").strip().lower()

    #End the game if player doesn't want to play anymore
    if continue_game == 'no':
        print("Exiting the Game!!")
        print("thank you for playing!!!!")

