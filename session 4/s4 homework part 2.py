import random

lottery_number= [19, 15, 11, 4, 17, 12, 18]
print('Your numbers are the following {}'.format(lottery_number))

no1= random.randint(1,20)
no2= random.randint(1,20)
no3= random.randint(1,20)
no4= random.randint(1,20)
no5= random.randint(1,20)
no6= random.randint(1,20)
no7= random.randint(1,20)

lotto_num= no1, no2, no3, no4, no5, no6, no7
six_nos= no1, no2, no3, no4, no5,no6
five_nos= no1, no2, no3, no4, no5
four_nos = no1,no2,no3,no4,
three_nos= no1, no2, no3


print('And the lottery numbers are: {}'.format(lotto_num))

if 'lotto_num'== lottery_number:
    print('You have won £1000000, All your numbers matched!')

elif six_nos in lottery_number:
    print('Youve won £10000 as six of your numbers matched')

elif five_nos in lottery_number:
    print('Youve won £100 as five of your numbers matched')

elif four_nos in lottery_number:
    print('Youve won £40 as four numbers matched')

elif three_nos in lottery_number:
    print('Youve won £20')

else: print('lose')










