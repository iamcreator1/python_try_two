previous_data = float(input('Введите предыдущие показания: '))
present_data =  float(input('Введите текущие показания: '))
price_m3 = float(input('Введите текущую стоимость за м3: '))

difference = present_data - previous_data
calculated_price = difference * price_m3

print(f'К оплате {calculated_price:.2f}')