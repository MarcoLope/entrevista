# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["0"],
        # Outputs
        ["Enter tree height: "],
        # Message in case of failure
        "Tree of height 0"
    ),
    # Test case 2
    (
        # Inputs
        ["3"],
        # Outputs
        ["Enter tree height: ", "  *", " * *", "* * *"],
        # Message in case of failure
        "Tree of height 3"
    ),
    # Test case 3
    (
        # Inputs
        ["6"],
        # Outputs
        ["Enter tree height: ", "     *", "    * *", "   * * *", "  * * * *", " * * * * *", "* * * * * *"],
        # Message in case of failure
        "Tree of height 6"
    ),
]
