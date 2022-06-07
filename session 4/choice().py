import random
first_names = ['bob', 'janet', 'chris', 'amelie', 'kate']
last_names = ['encona', 'harrer', 'smith', 'chanel']

chosen_first_name = random.choice(first_names)
chosen_second_name= random.choice(last_names)
print('{} {}'.format(chosen_first_name,chosen_second_name))