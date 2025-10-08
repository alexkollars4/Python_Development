#Simple Python program to calculate age based on user input

#Variable for user name input
user_name = input('Enter your name: ')
#Variable for user birth year input    
birth_year = int(input('Enter your Birth Year: '))
#Variable for current year input
current_year = int(input('Enter CurrentYear: ' ))

def  calculate_age(birth_year, current_year):
    return current_year - birth_year

print(f'Hello (user_name), you are years old.')
