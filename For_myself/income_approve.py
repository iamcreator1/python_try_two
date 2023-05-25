print('Вас приветствует программа IncomeTax')




while True:
    start_programm = input(f'Начать использование? "Да" / "Нет"\n-->>')
    if start_programm.lower() == 'да':
        income = float(input('Введите сумму вашего дохода\n-->>'))
        bils = float(input('Введите процент, который вам нужно заплатить\n-->>'))
        should_pay = income / 100 * bils
        after_bils = income - should_pay
        print(f'Ваш налог составляет {should_pay}')


        while True:
            clear_income = str(input('Хотите узнать вашу чистую прибыль? "Да"/"Нет"\n-->>'))
            if clear_income.lower() == 'да':
                print(f'Ваша чистая прибыль составляет {after_bils}')
                goods = str(input('Хотите отнять какие-то доп. расходы от вашей чистой прибыли? "Да"/"Нет"'))
                if goods.lower() == 'да':
                    expenses_sum = 0
                    while True:
                        expenses = input('Введите ваши расходы. Чтоб остановить введите "sum"\n-->>')
                        try:
                            float_expenses = float(expenses)
                            after_bils = after_bils - float_expenses
                            expenses_sum = expenses_sum + float_expenses
                        except:
                            if expenses.find('sum') != -1:
                                print(f'Расходы на сумму - "{expenses_sum}"\nЧистый остаток после расходов "{after_bils}"')
                                exit()
                            else:
                                print('Я не понял вашу команду')
                elif goods.lower() == 'нет':
                    print(f'Спасибо за использование программы IncomeTax. Ваша чистая сумма на руках - {after_bils}')



            elif clear_income.lower() == 'нет':
                print('Спасибо за использование IncomeTax. Good luck!')
                exit()

            else:
                print('Мне непонятная данная команда, введите "Да" или "Нет"')

    elif start_programm.lower() == 'нет':
        print('Спасибо за использование IncomeTax. Good luck!')
        break
    else:
        print('Мне непонятная Ваша команда. Введите "Да" или "Нет"')



