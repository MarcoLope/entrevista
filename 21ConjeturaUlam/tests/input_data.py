# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["0"],
        # Outputs
        ["Enter a number: ", "Invalid input"],
        # Message in case of failure
        "Invalid input"
    ),
    # Test case 2
    (
        # Inputs
        ["1"],
        # Outputs
        ["Enter a number: ", "1"],
        # Message in case of failure
        "Number 1 is already the end"
    ),
    # Test case 3
    (
        # Inputs
        ["2"],
        # Outputs
        ["Enter a number: ", "2 1"],
        # Message in case of failure
        "Number two is only divided by 2"
    ),
    # Test case 4
    (
        # Inputs
        ["3"],
        # Outputs
        ["Enter a number: ", "3 10 5 16 8 4 2 1"],
        # Message in case of failure
        "Number 3 requires multiple steps"
    ),
    # Test case 5
    (
        # Inputs
        ["46"],
        # Outputs
        ["Enter a number: ", "46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1"],
        # Message in case of failure
        "A longer sequence"
    ),
]
