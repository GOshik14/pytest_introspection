import pytest
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source")
import source.my_functions as my_funcs


### Simple math tests ###

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),    
    (1, -2, -1),
], ids = ["int_positive", "int_negative", "int_both_neg_pos"])
def test_add(a, b, expected):
    assert my_funcs.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2),
    (-4, -2, 2),    
    (-4, 2, -2)
], ids = ["positive", "negative", "both_neg_pos"])
def test_divide_positive(a, b, expected):
    assert my_funcs.divide(4, 2) == 2

#### Catching exceptions tests ####

@pytest.mark.generated_exception
def test_add_catch_exception_int_str():
    with pytest.raises(ValueError):
        my_funcs.add(1, "1")

@pytest.mark.generated_exception
def test_add_catch_exception_int_float():
    with pytest.raises(ValueError):
        my_funcs.add(1, 1.)

@pytest.mark.generated_exception
def test_add_catch_exception_str_float():
    with pytest.raises(ValueError):
        my_funcs.add("1", 1.)


@pytest.mark.generated_exception
def test_divide_catch_value_exception_int_str():
    with pytest.raises(ValueError):
        my_funcs.divide(1, "1")

@pytest.mark.generated_exception
def test_divide_catch_value_exception_int_float():
    with pytest.raises(ValueError):
        my_funcs.divide(1, 1.)

@pytest.mark.generated_exception
def test_divide_catch_value_exception_str_float():
    with pytest.raises(ValueError):
        my_funcs.divide("1", 1.)

@pytest.mark.generated_exception
def test_divide_catch_arithm_exception_0_0():
    with pytest.raises(ArithmeticError):
        my_funcs.divide(0, 0)

@pytest.mark.generated_exception
def test_divide_catch_arithm_exception_1_0():
    with pytest.raises(ArithmeticError):
        my_funcs.divide(1, 0)
