
from Code.Square import Square
import pytest
import sys

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


# TEST 11
# Testing if skipping a test works

@pytest.mark.skip(reason="Missing functionality")
def test_skip():
    print("Skipped test case")

# TEST 12
# Testing if 'skip if' works

@pytest.mark.skipif(sys.platform!=("darwin"), reason="Perform test only on Mac OS X systems")
def test_platform():
    print(sys.platform)
    print("You should see this only if you are running on a MAC OS X platform")

# TEST 13
@pytest.mark.skipif(sys.platform==("darwin"), reason="Perform test only if it is not a MAC OS X system")
def test_not_platform():
    print("You should see this only if you are running on a non MAC OS X platform")
