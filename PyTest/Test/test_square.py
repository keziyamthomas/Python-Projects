
from Code.Square import Square
import pytest

# TEST 1
# testing square function
def test_square():
    s = Square()
    assert s.square(5)==25

# TEST 2
# testing square of float
def test_sqrt():
    s = Square()
    assert s.squareroot(25)==5

# doing the same thing using fixtures
@pytest.fixture
def sq_instance():
    return Square()

# TEST 3
def test_square_fix(sq_instance): # parameter name should be same as fixture name
    assert sq_instance.square(5)==25

# TEST 4
def test_sqrt_fix(sq_instance):
    assert sq_instance.squareroot(25)==5

# TEST 5
# testing the function with different data types
def test_sqrt_int(sq_instance):
    assert sq_instance.square(3)==9

# TEST 6
def test_sqrt_float(sq_instance):
    assert sq_instance.square(3.3)==pytest.approx(10.89)

# TEST 7, TEST 8, TEST 9
# doing the same using parametrize
@pytest.mark.parametrize("num,expected", [
    (3, 9),
    (3.3, 10.89),
    (-8, 64),
])
def test_square_types(sq_instance,num,expected):
    assert sq_instance.square(num)==pytest.approx(expected)


# TEST 10
# Test for exceptions

def test_square_typerror(sq_instance):
    with pytest.raises(TypeError) as e:
        sq_instance.square("string")
    # assert str(e.value)
    print(str(e.value))  # use -s flag while running pytest to see what this statement prints

