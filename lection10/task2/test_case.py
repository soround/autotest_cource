# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_division_positive_numbers():
    assert all_division(10, 2, 5) == 1


def test_division_negative_numbers():
    assert all_division(-10, 2, -5) == 1


def test_division_fractional_numbers():
    assert all_division(10.0, 2.5) == 4.0


@pytest.mark.smoke
def test_division_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0, 5)


def test_division_single_number():
    assert all_division(10) == 10
