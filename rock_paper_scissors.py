import random

rock = 1
scissors = 2
paper = 3

player = int(input("Enter 1 for Rock, 2 for Scissors, 3 for Paper: "))


computer = random.randint(1, 3)

if player == computer:
    print("It's a tie! Try again!")
elif (player == rock and computer == scissors) or \
     (player == scissors and computer == paper) or \
     (player == paper and computer == rock):
    print("You win!")
else:
    print("Computer wins!")