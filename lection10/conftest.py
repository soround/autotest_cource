import pytest
import time


@pytest.fixture(scope="class")
def class_fixture(request):
    start_time = time.time()
    yield
    end_time = time.monotonic()
    duration = end_time - start_time
    print(f"\nClass {request.cls.__name__} execution time: {duration} seconds")


@pytest.fixture()
def test_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    duration = end_time - start_time
    print(f"Test execution time: {duration} seconds")
