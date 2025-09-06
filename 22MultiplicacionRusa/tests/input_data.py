# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["8", "0"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "0"],
        # Message in case of failure
        "Multiplication by 0"
    ),
    # Test case 2
    (
        # Inputs
        ["0", "5"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "0 5", "0 2", "0 1", "0"],
        # Message in case of failure
        "Multiplication by 0"
    ),
    # Test case 3
    (
        # Inputs
        ["1", "3"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "1 3", "2 1", "3"],
        # Message in case of failure
        "Multiplication by 1"
    ),
    # Test case 4
    (
        # Inputs
        ["7", "1"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "7 1", "7"],
        # Message in case of failure
        "Multiplication by 1"
    ),
    # Test case 5
    (
        # Inputs
        ["6", "8"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "6 8", "12 4", "24 2", "48 1", "48"],
        # Message in case of failure
        "6 x 8 = 48"
    ),
    # Test case 6
    (
        # Inputs
        ["23", "17"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "23 17", "46 8", "92 4", "184 2", "368 1", "391"],
        # Message in case of failure
        "23 x 17 = 391"
    ),
    # Test case 7
    (
        # Inputs
        ["17", "23"],
        # Outputs
        ["Enter factor 1: ", "Enter factor 2: ", "17 23", "34 11", "68 5", "136 2", "272 1", "391"],
        # Message in case of failure
        "17 x 23 = 391"
    ),
]
