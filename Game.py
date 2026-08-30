"""
WORKFLOW OF PROJECT:
1- Input from the user(rock, paper, scissor)
2- computeer choice(computer will choose randomly not conditionally)
3- Result print

cases:
A- Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = rock win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random
item_list = ["Rock", "Paper", "Scissor"]


user_choice = input("Enter your move = Rock, Paper , Scissor= ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {computer_choice}")

if user_choice == computer_choice:
            print("Both chooses same: Match tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers rock = Computer wins")

    else:
        print("Rock smashes Scissors = You win")

elif user_choice == "Paper":
    if computer_choice == "Scissors":
        print("Scissors cut paper = Computer wins")
    else:
        print("Paper covers Rock = You win")

else:
    if computer_choice == "Rock":
        print("Rock smashes Scissors = Computer wins")
    else:
        print("Scissors cut paper = You win")

