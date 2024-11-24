import random
#function
def get_choices ():
    #this is a list
    options = ["rock", "paper", "scissor"]
    #variable       assigning string
    player_choice = input ("Enter a choice Rock, Paper, Scissor: ")
    #a varaible with random library
    Computer_choice = random.choice(options)
    choices= {"player": player_choice, "computer": Computer_choice}

    return choices
   

def check_win (player, computer):
    print (f"player chose: {player}, computer chose: {computer}.")
    if player == computer:
        return "its a tie"
    elif player == "rock":  
        if computer == "scissor": 
            return "player win"
        else:
            return "computer win"
    elif player == "paper":
        if computer == "rock":  
            return "player win"
        else: 
            return "computer win"
    elif player == "scissor":
        if computer == "paper":
            return "player win"
        else: 
            return "computer win"
        
    
choices = get_choices()
result = check_win (choices["player"], choices ["computer"])
print (result)

