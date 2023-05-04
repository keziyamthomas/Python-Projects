# 

To run this code, follow the steps below:

1. Install pytest module

pip install pytest

2. Run pytest from the root directory i.e, PyTest in this case
Pytest will find the tests and run them

python -m pytest


pytest.fixture - A function in Pytest that allows same code to be used in multiple tests.
When fixture function is attached to a test function, it will return the data to the test before execution.

pytest.mark.parametrize - allows parameterization of arguments to a test function. Using this multiple inputs can be test using the same test function without duplicating the code. 
