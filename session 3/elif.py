oven_temperature = int(input('What is the temperature of your oven? '))
if oven_temperature > 200:
    print('The oven is too hot')
elif oven_temperature < 150:
    print('The oven is too cold')
elif oven_temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough mate')