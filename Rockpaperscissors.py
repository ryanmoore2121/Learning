import random
import time

#Create a list for all the options that the computer can pick and then make a variable that picks one
options = ["Rock", "Paper", "Scissors"]
getrandom = random.choice(options)

#Get players name
def playersname():
    playername = input("Hello, welcome to the rock, paper, scissors game. What is your name? ")
    return playername
    

# Function to pick choices and have computer generate a random choice
def gamechoices():
    playerchoice = input("Enter your choice rock, paper, or scissors: " ).capitalize()
    Computerchoice = getrandom
    choices = {"player": playerchoice, "computer": Computerchoice}
    return choices 
 

#Function to check who won the game through if statements
def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}.")
    if player == computer:
        return "Its a tie"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock beats scissors! YOU WIN!"
        else:
            return "Paper beats rock... You lose :'("
    elif player == "Scissors":
        if computer == "Rock":
            return "Rock beats scissors... You lose :'("
        else:
            return "Scissors cuts paper! YOU WIN!"
    elif player == "Paper":
        if computer == "Rock":
            return "Rock beats paper! YOU WIN!"
        else:
            return "Scissors beats paper... You lose :'("

#Calls the functions to greet the player
name = playersname()
startgame = print(f"Hello {name}, let's play rock, paper, scissors!")

#Wait one seconds
time.sleep(1)

#Calls the function to get a selection
choices = gamechoices()

#Wait one seconds
time.sleep(1)

#Calls the function to get the results of the game
result = check_win(choices["player"], choices["computer"])
print(result)