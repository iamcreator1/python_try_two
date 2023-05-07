print('Hey, how much money do your have?')
amount = float(input('I have = '))
cookie = float(input('Please, enter price for cookie here = '))
candy = float(input('Please, enter price for candy here = '))

totalPrice = cookie + candy
if amount >= totalPrice:
    print('Hey, u have enough money')
else:
    print('Hey, not enough money in here!')
