meal_price= float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount for your order? (Y/N) ')
discount_applicable = discount_choice == 'Y'
discounted_price = meal_price > 20.00

if discount_applicable and discounted_price:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')

print('Discounted cost: {}'.format(meal_price))