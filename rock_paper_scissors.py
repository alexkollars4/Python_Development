import random

rock = 1
scissors = 2
paper = 3

input = int(input("Enter 1 for Rock, 2 for Scissors, 3 for Paper: "))

player = input
computer = 1 

if player == computer:
    print("It's a tie!")
elif player == rock and computer == scissors:
    print("You win! Rock crushes Scissors.")
elif player == scissors and computer == paper:
    print("You win! Scissors cut Paper.")
elif player == paper and computer == 11:
    print("You win! Paper covers Rock.")