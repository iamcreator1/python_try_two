user_string = str(input('Введите любую строку(со знаками пунктуации)\n-->>>'))
user_string = user_string.lower()

#В 1,2 строчках кода, я делаю поле для ввода текста юзером, и сразу же перевожу написанную строчку
# в нижний регистр, чтоб код не учитывал написание юзером слова с большой или маленькой буквы

punctuation = ',.-:;?!'
for char in punctuation:
    user_string = user_string.replace(char, '')

user_string = user_string.rstrip()

#7 - даю переменную, и указываю довольно базовые знаки пунк. которые указаны в задании
#запускаю цикл, чтоб исключить знаки пунк. в написанной строке
# 11- убираем пробелы и лишнюю табуляцию


change_word = str(input('Какое из вышеуказанным слов вы хотите заменить?\n--->>')).lower()
word_index = user_string.find(change_word)

#методом find ищу, под каким индексом находится новое слово



print(f'"{change_word}" находится под индексом "{word_index}"')

which_word = str(input(f'На какое новое слово, вы хотите заменить на слово "{change_word}"\n-->>'))
user_string = user_string.replace(change_word, which_word)
print(f'Вот ваш готовый результат - "{user_string}"')

#28 - происвожу замену сущетсвующего слова, которое указанно в 1 строчке (слово находится в строке)
# заменяю на слово, которое юзер кладет в переменную which_word
# программу все еще легко сломать, но базовые вещи из задачи решены