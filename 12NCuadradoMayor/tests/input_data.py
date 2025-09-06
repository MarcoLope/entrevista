# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["25"],
        # Outputs
        ["Escribe un numero : ", "6"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado"
    ),
    # Test case 2
    (
        # Inputs
        ["155"],
        # Outputs
        ["Escribe un numero : ", "13"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado"
    ),
    # Test case 3
    (
        # Inputs
        ["12090"],
        # Outputs
        ["Escribe un numero : ", "110"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado"
    ),
    # Test case 4
    (
        # Inputs
        ["0"],
        # Outputs
        ["Escribe un numero : ", "1"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    ),# Test case 5
    (
        # Inputs
        ["1"],
        # Outputs
        ["Escribe un numero : ", "2"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    ),
]
