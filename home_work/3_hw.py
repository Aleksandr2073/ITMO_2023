def numbers(num_1, num_2):
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)

numbers(77, 888)



def numbers_2(num_3, num_4):
    if (num_3 - num_4) == 135 or (num_4 - num_3) == 135:
        print('Yes')
    else:
        print('No')

numbers_2(7, 102)


def season(month):
    if month in range(1, 3) or month == 12:
        print('Зима')
    elif month in range(3, 6):
        print('Весна')
    elif month in range(6, 9):
        print('Лето')
    else:
        print('Осень')

season(11)


def numbers_3(a, b, c):
    if a > 10 and b > 10 and c >10:
        print('Yes')
    else:
        print('No')

numbers_3(11, 44, 77)
numbers_3(11, 44, 7)



def day(year: int, month: int):
    return (year * 12 + month) * 29
print(day(2, 10))