"""
Evaluating the results of a function

Using Python decorators and parametrize to add multiple independent tests
This allows each test to be evaluated independently
"""

import pytest
from src.main import parking_cost

# Decorator to indicate the arguments to the test function
@pytest.mark.parametrize('hours, minutes, result, message',
                         # The input, output and message in case of failure
                         [
                          (0, 0, 0, 'Pay $0 if there is no time'),
                          (0, 10, 5, 'Pay $5 for the first 2 hours'),
                          (1, 40, 5, 'Pay $5 for the first 2 hours'),
                          (2, 30, 17, 'During the third hour, pay $ 5 + 12'),
                          (3, 1, 22, 'For 3:01, pay $ 5 + 12 + 5'),
                          (3, 20, 25, 'For 3:20, pay $ 5 + 12 + 5 + 3'),
                          (4, 31, 39, 'For 4:31, pay $ 5 + 12 + 12 + 5 + 3 + 2'),
                          (6, 50, 65, 'For 4:31, pay $ 5 + 12 + 12 + 12 + 12 + 5 + 3 + 2 + 2'),
                         ])
# Simple function to run all the asserts
def test_function(hours, minutes, result, message):
    assert parking_cost(hours, minutes) == result, message
