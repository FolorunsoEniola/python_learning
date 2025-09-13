import random

def new_game():
    user_choice = input('choose a number from 1-9 or enter exit to quit:')
    computer_guess = random.randint(1,9)
    
    if user_choice.lower() == 'exit':
        return('Thanks for breaking')
    user_pick = int(user_choice)
    if computer_guess == user_pick:
        return('Yay, you guessed right.')
    if user_pick < 1 or user_pick > 9:
        return('invalid input, please choose between 1 - 9')
    if computer_guess > user_pick:
        return(f'Oh no your choice is too low, the computer choice is {computer_guess}')
    if computer_guess < user_pick:
        return(f'sorry, your guess is too high, the computer choice is {computer_guess}')

    
    
print(new_game())
