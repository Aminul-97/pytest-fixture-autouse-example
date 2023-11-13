import pytest
 
num = 5

@pytest.fixture(autouse=True)
def setup_fixture1():
    print("\nExecuting autouse fixture 1")
    global num
    num = 1

@pytest.fixture(autouse=True)
def setup_fixture2():
    print("\nExecuting autouse fixture 2")
    global num
    num += 2

@pytest.fixture(autouse=True)
def setup_fixture3():
    print("\nExecuting autouse fixture 3")
    global num
    num += 3

def test_example():
    print("Executing the test")
    assert num == 6