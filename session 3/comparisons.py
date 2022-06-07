price = input('What is the price of the burger? ')
vegetarian = input('Is the restaurant Vegetarian Y/N')
is_price = float(price) <= 10.00
is_vegetarian = vegetarian == 'Y'
can_i_buy = is_vegetarian and is_price
print('You should buy the burger: {}'.format(can_i_buy))



