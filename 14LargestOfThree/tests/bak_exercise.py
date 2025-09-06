"""
Evaluating the results of a function

Using Python decorators and parametrize to add multiple independent tests
This allows each test to be evaluated independently
"""

import pytest
from src.main import largest_of_three

# Decorator to indicate the arguments to the test function
@pytest.mark.parametrize('a, b, c, result, message',
                         # The input, output and message in case of failure
                         [
                          (5, 3, 8, 8, 'Last number is the largest'),
                          (2, 4, 8, 8, 'Last number is the largest'),
                          (5, 3, 1, 5, 'First number is the largest'),
                          (5, 3, 4, 5, 'First number is the largest'),
                          (2, 6, 1, 6, 'Second number is the largest'),
                          (5, 6, 3, 6, 'Second number is the largest'),
                          (2, 2, 2, 2, 'All numbers equal')
                         ])
# Simple function to run all the asserts
def test_function(a, b, c, result, message):
    assert largest_of_three(a, b, c) == result, message
