import pytest


@pytest.fixture(autouse=True)
def set_number():
    return 50


def test_example(set_number):
    # Your test code here
    print("Executing the test")
    assert set_number == 50
