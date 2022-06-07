shopping_list= ['bread', 'milk', 'eggs', 'chocolate']

if 'bread' in shopping_list:
    shopping_list.append ('butter')
print('Your shopping list {}'.format(shopping_list))

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost
    print(total_cost)

print(round(total_cost, 2))


