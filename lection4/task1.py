# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон  треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def is_valid_triangle(side_a, side_b, side_c):
    return not((side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a))


def which_triangle(a, b, c):
    if not is_valid_triangle(side_a=a, side_b=b, side_c=c):
        return "Не треугольник"

    if a == b == c:
        type_triangle = "Равносторонний"
    elif a == b or b == c or c == a:
        type_triangle = "Равнобедренный"
    else:
        type_triangle = "Обычный"

    return type_triangle


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]

for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
