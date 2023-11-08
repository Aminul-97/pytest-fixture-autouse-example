import pytest
from src.number_conversions import Number_conversion


# Fixture that holds the list of numbers
@pytest.fixture
def list_num():
    return []

# Fixture  that initializes classes
@pytest.fixture
def initiate_class(list_num):
    return Number_conversion(list_num[0]), Number_conversion(list_num[1]), Number_conversion(list_num[2])


# Autouse fixture that creates a list of number
# Executes before each test
@pytest.fixture(autouse=True)
def setup_test(list_num):
    print("\nAUTOUSE fixture running...")
    list_num.append(30)
    list_num.append(40)
    list_num.append(60)

# Testing binary conversion
def test_convert_to_binary(initiate_class):
    assert initiate_class[0].convert_to_binary() == "0b11110"

# Testing Octal conversion
def test_convert_to_octal(initiate_class):
    assert initiate_class[1].convert_to_octal() == "0o50"

# Testing Hexadecimal conversion
def test_convert_to_hexadecimal(initiate_class):
    assert initiate_class[2].convert_to_hexadecimal() == "0x3c"



