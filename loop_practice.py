loop_count = 0 

continue_loop = input('Do you want to continue the loop (y/n): ')
#loops and counts up every time y is entered
while continue_loop == 'y' or continue_loop == 'Y':
    loop_count += 1 
    continue_loop = input('Do you want to continue the loop (y/n): ')
 #Prints when y is not entered    
print(f'The loop ran {loop_count} times.')
        