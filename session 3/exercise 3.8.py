import random
def colour():
    random_number = random.randint(1,2)

    if random_number == 1:
        colour='red'

    else:
        colour='black'

    return colour

random_number = random.randint(1,100)
random_number= colour()

bet_amount = int(input('How much do you want to bet?'))
colour_choice = input('Red or Black?')
number_choice = int(input('Choose a number between 1-100'))
doubled = bet_amount * 2
hundred = bet_amount * 100
if colour_choice == colour():
    print('Keep your bet')

elif number_choice == random_number:
    print ('You have won {}'.format(doubled))

elif colour_choice == random_number:
    print ('You have won {}'.format(hundred))

else:
    print('You win nothing 0')


