# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII
import math


def to_roman(val):
    romans_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "G",
        10000: "H"
    }

    div = 1
    while val >= div:
        div *= 10

    div /= 10

    str_roman = ""

    while val:
        last_num = int(val / div)

        if last_num <= 3:
            str_roman += (romans_dict[div] * last_num)
        elif last_num == 4:
            str_roman += (romans_dict[div] + romans_dict[div * 5])
        elif 5 <= last_num <= 8:
            str_roman += (romans_dict[div * 5] + (romans_dict[div] * (last_num - 5)))
        elif last_num == 9:
            str_roman += (romans_dict[div] + romans_dict[div * 10])

        val = math.floor(val % div)
        div /= 10

    return str_roman


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']

for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
