
print('Slava to Ukraine BOT!')

while True:
    message = str(input()).lower()

    if message == 'привіт' or message == 'хай' or message == 'доброго дня':
        print('Доброго вечора, я бот з України!')
    elif message == 'як справи?' or message == 'що робиш?' or message == 'чим займаешься?':
        print('Вчусь програмувати на Python!')
    elif message.find('фільм') != -1 or message.find('серіал') != -1 or message.find('кінотеатр') != -1:
        print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться \'Whiplash\', він просто бомба!')
    elif message.find('бувай') != -1 or message.find('надобраніч') != -1 or message.find('гудбай') != -1 or message.find('До зустрічі') != -1:
        print('Побачимось у мережі, I\'ll be back.')
        break
    else:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')