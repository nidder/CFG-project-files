import random
def random_choice():
    choice_number=random.randint(1,3)

    if choice_number == 1:
        choice= ' rock'
    elif choice_number == 2:
        choice =' scissors'
    else:
        choice =' paper'

    return choice

my_choice = input ('Choose rock, scissors, paper: ')
opponent_choice= random_choice()
user_choice = my_choice == 'rock' or my_choice == 'paper' or my_choice == 'scissors'

print('Your opponent chose{}'.format(opponent_choice))

if user_choice:
    print('Request completed - success')
if not user_choice:
    print('failure, enter rock, paper or scissors')

if my_choice =='rock' and opponent_choice ==' scissors':
    print('You win!')
elif my_choice == 'rock' and opponent_choice == ' rock':
    print('Its a draw!')
elif my_choice == 'rock' and opponent_choice == ' paper':
    print('You lose!')

if my_choice == 'scissors' and opponent_choice == ' scissors':
    print('Its a draw')
elif my_choice == 'scissors' and opponent_choice == ' rock':
    print('You lose!')
elif my_choice == 'scissors' and opponent_choice == ' paper':
    print('You win!')

if my_choice == 'paper' and opponent_choice == ' paper':
    print('Its a draw')
elif my_choice == 'paper' and opponent_choice == ' rock':
    print('You win')
elif my_choice == 'paper' and opponent_choice == ' scissors':
    print('You lose!')


