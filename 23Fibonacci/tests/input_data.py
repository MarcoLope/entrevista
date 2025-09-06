# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["0"],
        # Outputs
        ["Enter the index: ", "0"],
        # Message in case of failure
        "The sequence starts at 0"
    ),
    # Test case 2
    (
        # Inputs
        ["1"],
        # Outputs
        ["Enter the index: ", "1"],
        # Message in case of failure
        "The second number is 1"
    ),
    # Test case 3
    (
        # Inputs
        ["2"],
        # Outputs
        ["Enter the index: ", "1"],
        # Message in case of failure
        "0 + 1 = 1"
    ),
    # Test case 4
    (
        # Inputs
        ["7"],
        # Outputs
        ["Enter the index: ", "13"],
        # Message in case of failure
        "Fibonacci at index 7"
    ),
    # Test case 5
    (
        # Inputs
        ["35"],
        # Outputs
        ["Enter the index: ", "9227465"],
        # Message in case of failure
        "Larger Fibonacci numbers"
    ),
]
