import pytest

@pytest.fixture(autouse=True)
def multiply_fixture(request):
    num = request.param
    yield num

@pytest.mark.parametrize("multiply_fixture", [2, 3, 4], indirect=True)
def test_multiplication(multiply_fixture):
    assert multiply_fixture*5 != None