
#For loop that iterates from 0 to 4 which is 5 iterations
for count in range(1):
    #Prints the current count value alwasy starting from 0
    print(count)
    

#Iterates from 2 to 5 which is 4 iterations. Starts at 2. 
for count in range(-2, 6):  
    
    print(count)

#Iterates from 0 to 9 but with a step of 2. 
#So it prints only even numbers and stops at since 10 is not included.
for count in range(0, 10, 2):  
    print(count)


count = 0
number = int(input("Enter a integer: "))

for count in range(1,11):
    
    print(number, "x", count, "=", number * count)