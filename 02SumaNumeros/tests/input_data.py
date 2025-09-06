# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["1","2","0"],
        ["","","","3"],
        "Debe salir\n3"
    ),
    (
        ["1","-1","0"],
        ["","","","0"],
        "Debe salir\n0"
    ),
    (
        ["1","2","3","0"],
        ["","","","","6"],
        "Debe salir\n6"
    ),
    (
        ["100","200","0"],
        ["","","","300"],
        "Debe salir\n300"
    )
]
