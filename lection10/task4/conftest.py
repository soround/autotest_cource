import pytest
import datetime


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    start_time = datetime.datetime.now()
    print(f"Test session started at {start_time}")

    yield

    end_time = datetime.datetime.now()
    print(f"Test session ended at {end_time}")


@pytest.fixture
def test_fixture(request):
    start_time = datetime.datetime.now()
    print(f"Test '{request.node.name}' started at {start_time}")

    yield

    end_time = datetime.datetime.now()
    print(f"Test '{request.node.name}' ended at {end_time}")
