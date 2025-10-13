#Simple Python program to calculate age based on user input

#Variable for user name input
user_name = input('Enter your name: ')

#variable for favorite hobby input
favorite_hobby = input('Enter your favorite hobby: ')

#Variable for user birth year input    
birth_year = int(input('Enter your Birth Year: '))

#Variable for current year input
current_year = int(input('Enter Current Year: ' ))

#Method to calculate age
current_age = current_year - birth_year

print(f'Hello {user_name}, you are {current_age} years old and enjoy {favorite_hobby}.')
