# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["0", "0"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: Origin"],
            'Both coordinates are at 0',
        ),
        # Test case 2
        (
            ["0", "10"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: Y axis"],
            'X is equal to 0',
        ),
        # Test case 3
        (
            ["5.8", "0"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: X axis"],
            'Y is equal to 0',
        ),
        # Test case 4
        (
            ["3.2", "2"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: I"],
            'First quadrant',
        ),
        # Test case 5
        (
            ["-1", "4"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: II"],
            'Second quadrant',
        ),
        # Test case 6
        (
            ["-3", "-0.3"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: III"],
            'Third quadrant',
        ),
        # Test case 7
        (
            ["6.2", "-4"],
            ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: IV"],
            'Fourth quadrant',
        ),
    ]
