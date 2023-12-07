num = -0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


def yes_no(str_1, str_2):
    if str_1 in str_2:
        print('Да')
    else:
        print('Нет')

yes_no(str_1= 'test', str_2= 'test1')



num_float = 0

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


year = 5

if year == 1 or year == 2 or year == 3 or year == 4:
    print('Бакалавр')
elif year == 5 or year == 6:
    print('Магистр')
elif year == 7 or year == 8 or year == 9:
    print('Аспирант')
else:
    print('Введите корректный год обучения')



def student(year_of_study):
    if year_of_study in range(1, 5):
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистр')
    elif year_of_study in range(7, 10):
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student(8)


def num(number):
    if number > 100 or number < -100:
        print('-')
    else:
        print('+')

num(77)


a = 5

if a > 100 or a < -100:
    print('-')
else:
    print('+')