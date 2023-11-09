import pytest
from src.number_conversions import NumberConversions


# Define a fixture to yield a static number with a `autouse=True` and session scope i.e the number is created once for all the tests
@pytest.fixture(autouse=True, scope="session")
def static_number():
    print("\nAUTOUSE fixture `static_number` setup...")
    yield 50
    print("\nAUTOUSE fixture `static_number` teardown...")


# Define a fixture to create an instance of NumberConversions with a function scope i.e the instance is created for each test function
@pytest.fixture(scope="function")
def number_converter(static_number):
    return NumberConversions(static_number)


def test_convert_to_binary(number_converter):
    result = number_converter.convert_to_binary()
    assert result == "0b110010"


def test_convert_to_octal(number_converter):
    result = number_converter.convert_to_octal()
    assert result == "0o62"


def test_convert_to_hexadecimal(number_converter):
    result = number_converter.convert_to_hexadecimal()
    assert result == "0x32"
