# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["0"],
        # Outputs
        ["Enter pyramid height: ", "Out of range"],
        # Message in case of failure
        "Invalid input"
    ),
    # Test case 2
    (
        # Inputs
        ["27"],
        # Outputs
        ["Enter pyramid height: ", "Out of range"],
        # Message in case of failure
        "Invalid input"
    ),
    # Test case 3
    (
        # Inputs
        ["1"],
        # Outputs
        ["Enter pyramid height: ", "A"],
        # Message in case of failure
        "Pyramid of height 1"
    ),
    # Test case 4
    (
        # Inputs
        ["3"],
        # Outputs
        ["Enter pyramid height: ", "    A",
                                   "  A B A",
                                   "A B C B A"],
        # Message in case of failure
        "Pyramid of height 3"
    ),
    # Test case 5
    (
        # Inputs
        ["15"],
        # Outputs
        ["Enter pyramid height: ", "                            A", "                          A B A", "                        A B C B A", "                      A B C D C B A", "                    A B C D E D C B A", "                  A B C D E F E D C B A", "                A B C D E F G F E D C B A", "              A B C D E F G H G F E D C B A", "            A B C D E F G H I H G F E D C B A", "          A B C D E F G H I J I H G F E D C B A", "        A B C D E F G H I J K J I H G F E D C B A", "      A B C D E F G H I J K L K J I H G F E D C B A", "    A B C D E F G H I J K L M L K J I H G F E D C B A", "  A B C D E F G H I J K L M N M L K J I H G F E D C B A", "A B C D E F G H I J K L M N O N M L K J I H G F E D C B A"],
        # Message in case of failure
        "Pyramid of height 15"
    ),
]
