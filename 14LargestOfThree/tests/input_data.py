# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["5", "3", "8"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '8'],
            "Last number is the largest",
        ),
        # Test case 2
        (
            ["2", "4", "8"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '8'],
            "Last number is the largest",
        ),
        # Test case 3
        (
            ["5", "3", "1"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '5'],
            "First number is the largest",
        ),
        # Test case 4
        (
            ["5", "3", "4"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '5'],
            "First number is the largest",
        ),
        # Test case 5
        (
            ["2", "6", "1"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '6'],
            "Second number is the largest",
        ),
        # Test case 6
        (
            ["5", "6", "3"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '6'],
            "Second number is the largest",
        ),
        # Test case 7
        (
            ["2", "2", "2"],
            ["Enter first number: ", "Enter second number: ", "Enter third number: ", '2'],
            "All numbers are equal",
        ),
    ]
