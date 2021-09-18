import random
num = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку')
povtor = 'да'
num_polz = input('Введите число от 1 до 100:')
count = 0
while povtor.lower() == 'да':
    def is_valid(num_polz):
        if num_polz.isdigit() == True and 1 <= int(num_polz) <= 100:
            return True
        return False

    while True:
        num_polz = num_polz
        if is_valid(num_polz) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            num_polz = int(num_polz)
            break

    if num_polz < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
        num_polz = input('Введите число от 1 до 100:')
    elif num_polz > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
        num_polz = input('Введите число от 1 до 100:')
    else:
        count += 1
        print('Вы угадали, поздравляем!')
        print('Количество попыток', count)
        povtor = input('Хотите сыграть еще раз?Да, нет')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
