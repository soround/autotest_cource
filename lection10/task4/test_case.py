# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import pytest


@pytest.mark.usefixtures("session_fixture")
class TestClass:

    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2

    def test_three(self, test_fixture):
        assert 3 == 3

    def test_four(self):
        assert 4 == 4
