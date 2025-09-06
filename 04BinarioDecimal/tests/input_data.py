# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["Hola!"],
        ["", "-1"],
        "Debe salir: -1"
    ),
    (
        ["0a"],
        ["", "-1"],
        "Debe salir: -1"
    ),
    (
        ["1010"],
        ["", "15"],
        "Debe salir: 15"
    ),
    (
        ["1111111"],
        ["", "127"],
        "Debe salir: 127"
    )

]
