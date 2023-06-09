import datetime

import pytest


@pytest.fixture(scope="class", autouse=True)
def session_fixture():
    start_time = datetime.datetime.now()
    print(f"[] Тесты запущены в {start_time} ")

    yield

    end_time = datetime.datetime.now()
    print(f"[] Тесты закончены в {end_time} ")


@pytest.fixture(scope='function')
def test_fixture():
    start_time = datetime.datetime.now()
    print(f"[] Тест запущен в {start_time} ")

    yield

    end_time = datetime.datetime.now()
    print(f"[] Тест закончен в {end_time} ")
