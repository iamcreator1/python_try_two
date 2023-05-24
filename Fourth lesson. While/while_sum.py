user_sum = 0

while True:
    user_input = input('Введите любое число\n-->>')
    try:
        float_user_input = float(user_input)
        print(float_user_input)
        user_sum += float_user_input
    except:
        if user_input.find('sum') != -1:
            print(f'Сумма введеных чисел равна = {user_sum}')
            break
        else:
            print('Я не понял данную команду')


# user_sum = 0
#
# while True:
#     user_input = input('Введите любое число\n-->>')
#     try:
#         float_user_input = float(user_input)
#         print(float_user_input)
#         user_sum += float_user_input
#     except:
#         if user_input.find() == 'sum':
#             print(f'Сумма введеных чисел равна = {user_sum}')
#         break
