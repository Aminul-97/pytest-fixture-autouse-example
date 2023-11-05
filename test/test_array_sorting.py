import pytest
from src.array_sorting import arr_sorting


@pytest.fixture
def set_array():
    return []

@pytest.fixture
def initiate_class(set_array):
    return arr_sorting(set_array)

@pytest.fixture(autouse=True)
def setup_test(set_array):
    print("AUTOUSE fixture running")
    set_array.append(64)
    set_array.append(34)
    set_array.append(25)
    set_array.append(12)
    set_array.append(22)
    set_array.append(11)
    set_array.append(90)

def test_insertion_sort(initiate_class):
    assert initiate_class.insertion_sort() == [11, 12, 22, 25, 34, 64, 90]


def test_selection_sort(initiate_class):
    assert initiate_class.selection_sort() == [11, 12, 22, 25, 34, 64, 90]


def test_bubble_sort(initiate_class):
    assert initiate_class.bubble_sort() == [11, 12, 22, 25, 34, 64, 90]
