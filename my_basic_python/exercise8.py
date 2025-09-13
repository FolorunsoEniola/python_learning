import random
options = ['rock', 'paper', 'scissors']
#rock,paper,scissors game
#function to get user  choice, generate random for computer
#ensure entries are correct
def rock_paper():
    choice = random.choice(options)
    user_choice= input('input your choice:').lower()
    if user_choice.isdigit():
        print('please enter a word, not a number')
        return None, None
    elif user_choice not in options:
        print('please enter Rock, Paper, or Scissors')
        return None, None
    return choice, user_choice
# define function to determine tie,loss or win
def game_result(choice, user_choice):
    if choice == user_choice:
        print('It\'s a tie')
    elif user_choice == 'rock':
        if choice == 'scissors':
             print("You win! Rock crushes scissors.")
        else:
            print("You lose! Paper covers rock.")

    elif user_choice == "paper":
        if choice == "rock":
            print("You win! Paper covers rock.")
        else:
            print("You lose! Scissors cut paper.")

    elif user_choice == "scissors":
        if choice == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("You lose! Rock crushes scissors.")
    
choice , user_choice = rock_paper()
game_result(choice, user_choice)
print(f'The computer choice is {choice}')
