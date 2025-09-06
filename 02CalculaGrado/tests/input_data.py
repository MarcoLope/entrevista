# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["50"],
        ["Ingresa Un valor entre 0.0 y 1.0: ", "score incorrecto"],
        "Debe mostrar:\nscore incorrecto"
    ),
    (
        ["0.98"],
        ["Ingresa Un valor entre 0.0 y 1.0: ", "A"],
        "Debe mostrar:\nA"
    ),
    (
        ["0.65"],
        ["Ingresa Un valor entre 0.0 y 1.0: ", "D"],
        "Debe mostrar:\nD"
    ),
    (
        ["0.8"],
        ["Ingresa Un valor entre 0.0 y 1.0: ", "C"],
        "Debe mostrar:\nC"
    ),
    (
        ["-5.1"],
        ["Ingresa Un valor entre 0.0 y 1.0: ", "score incorrecto"],
        "Debe mostrar:\nscore incorrecto"
    )
]
