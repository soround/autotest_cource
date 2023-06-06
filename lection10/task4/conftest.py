import pytest
import datetime


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    start_time = datetime.datetime.now()
    print(f"Test session started at {start_time}")
    print()

    yield

    end_time = datetime.datetime.now()
    print(f"Test session ended at {end_time}")
    print()


@pytest.fixture
def test_fixture():
    start_time = datetime.datetime.now()
    print(f"Test started at {start_time}")
    print()

    yield

    end_time = datetime.datetime.now()
    print(f"Test ended at {end_time}")
    print()
