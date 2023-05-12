consumption = float(input('Введите расход топлива на 100 км вашего автомобиля: '))
gas_price = float(input('Сегодняшняя цена: '))
distance = float(input('Введите расстояние: '))

gas_spend = distance * consumption / 100
money_spend_for_gas = gas_spend * gas_price

print(f'На данное расстояние ({distance:.2f} km) потрачено такое кол-во топлива ({gas_spend:.2f} l), и сумма за оплату топлива равна {money_spend_for_gas:.2f} grn')

print('А теперь посчитай расход в милях!')

km_in_mile = 1.60934
consumption = float(input('Введите расход топлива на 100 миль вашего автомобиля: '))
gas_price = float(input('Сегодняшняя цена: '))
distance = float(input('Введите расстояние: '))

gas_spend_mile = distance * (consumption / km_in_mile) / 100
money_spend_for_gas_mile = gas_spend_mile * gas_price

print((f'На данное расстояние ({distance:.2f} km) потрачено такое кол-во топлива ({gas_spend_mile:.2f} l), и сумма за оплату топлива равна {money_spend_for_gas_mile:.2f} grn'))



