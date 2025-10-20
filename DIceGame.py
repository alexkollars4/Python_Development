import random

die1 = 6
print(f"Die 1: {die1}")
die2 = 6
print(f"Die 2: {die2}") 
total = die1 + die2

# My method 
if total == 7:
    print("You win!")
elif total == 11:
    print("You win!")
elif die1 == die2: 
    print("You win!")
    if die1== 6 and die2 ==6:
        print("Jackpot! You win!")
else:
    print("You lose!")

#class method
if total == 7 or total == 11:
    print("You win!")
elif die1 == die2:
    if die1 == 6:
        print("Jackpot! You win!")
else:
    print("You lose!")  
