shopping_list = ['oranges', 'cat food', 'sponge cake', 'long-grain rice','cheese board']
print(shopping_list[0])
#needs to start from number zero

chocolates = {
    'white':1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,

}

choc_price = input('Enter the chocolate type you desire:')

if 'white' == choc_price:
    print(chocolates['white'])

if 'milk' == choc_price:
    print(chocolates['milk'])
if 'dark' == choc_price:
    print(chocolates['dark'])
if 'vegan' == choc_price:
    print(chocolates['vegan'])




