'''
Exercise 10: Rock Paper Scissors Project
- Ask player if they choose rock, paper, or Scissors
- Have computer RANDOMLY choose one of the three
- Compare the choices and decide who wins
- Print result of game
'''
import random

# short options
def shortReponce(prompt, options):
    while True:
        user_input = input(prompt).strip().lower()
        for option in options:
            if user_input == option.lower():
                return option
        print("Invalid input, try again.")
        
def convert(user_input):
    if user_input in ['r', 'rock']:
        return 'Rock'
    elif user_input in ['p', 'paper']:
        return 'Paper'
    elif user_input in ['s', 'scissors']:
        return 'Scissors'
# loop
optionsList = ["Rock","Paper","Scissors"]
playerPoints = 0
ComputerPoints = 0
turns = 3
running = True
start = True
while running:
    if start:
        print("WOuld you like to play Rock Paper Scissors?")
        play = shortReponce("(Y | N): ", ["yes",'y',"no","n"])
        if play == "no" or play == "n":
            print("Thanks for playing!")
            running = False
        else:
            start = False
    elif not(start):
        print("Rock, Paper, Scissors, Shoot")
        computer_pick = random.choice(optionsList)
        user_pick = convert(shortReponce(f"{optionsList}: ", ["Rock",'r',"Paper","p","Scissors","s"])[0])
        print("Computer picked: ",computer_pick)
        if user_pick == computer_pick:
            print("It's a tie!")
        else:
            turns -= 1
            print(f"You have {turns} truns left")
            if (user_pick == "Rock" and computer_pick == "Scissors") or (user_pick == "Paper" and computer_pick == "Rock") or (user_pick == "Scissors" and computer_pick == "Paper"):
                print("You win this round")
                playerPoints += 1
            else:
                print("Computer wins this round")
                ComputerPoints += 1
        if turns <= 0:
            print("End of the game!\n")
            print(F"Your points {playerPoints} \t Computer Points {ComputerPoints}")
            if playerPoints > ComputerPoints:
                print("You win!")
            else:
                print("Computer wins!")
            start = True
    