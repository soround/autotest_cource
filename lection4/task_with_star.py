# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def increase_digit(all_digits, increment):
    for digit in range(len(all_digits)):
        if all_digits[digit] + increment < 10:
            all_digits[digit] += increment
            while all_digits[digit] + 3 < 10:
                all_digits[digit] += 3
            return all_digits
    return all_digits


def max_division_by_3(num):
    all_digits = [int(item) for item in list(str(num))]
    digit_sum = sum(all_digits)

    # if digit_sum < 10:
    #     return 9

    mod_division = digit_sum % 3
    increment = 3 - mod_division
    increase_digit(all_digits, increment)
    new_num = int(''.join(map(str, list(all_digits))))

    return new_num


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]

for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
