import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = input('heads or tails: ')
result = flip_coin()

winner = result == choice
user_choice = choice == 'heads' or choice == 'tails'

if not user_choice:
    print ('failure')
elif winner:
    print('you win')
else:
    print('you lose')

print('The coin landed on {}'.format(result))

