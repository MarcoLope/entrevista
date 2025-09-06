# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["56"],
            ["Enter grade: ", "Fail"],
            "Less than 70 fails",
        ),
        # Test case 2
        (
            ["69"],
            ["Enter grade: ", "Fail"],
            "Less than 70 fails",
        ),
        # Test case 3
        (
            ["82"],
            ["Enter grade: ", "Pass"],
            "More than 70 passes",
        ),
        # Test case 4
        (
            ["70"],
            ["Enter grade: ", "Pass"],
            "Exactly 70 passes",
        ),
    ]
