# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["5"],
        # Outputs
        ["Escribe un numero entero no negativo para calcular su factorial: ", "120"],
        # Message in case of failure
        "Revisa que estes haciendo bien las operaciones"
    ),
    # Test case 2
    (
        # Inputs
        ["0"],
        # Outputs
        ["Escribe un numero entero no negativo para calcular su factorial: ", "1"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    ),
    # Test case 3
    (
        # Inputs
        ["1"],
        # Outputs
        ["Escribe un numero entero no negativo para calcular su factorial: ", "1"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    ),
    # Test case 4
    (
        # Inputs
        ["-5"],
        # Outputs
        ["Escribe un numero entero no negativo para calcular su factorial: ", "Factorial no definido para negativos"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    ),
]
