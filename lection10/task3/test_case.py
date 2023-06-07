# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smoke, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("numbers, expected_result", [
    ((10, 2), 5),
    pytest.param((20, 4), 5, marks=pytest.mark.smoke),
    pytest.param((30, 0), None, marks=pytest.mark.skip(reason="Division by zero"))],
                         ids=["Test 1", "Test 2", "Test 3 (skipped)"])
def test_all_division(numbers, expected_result):
    result = all_division(*numbers)
    assert result == expected_result
