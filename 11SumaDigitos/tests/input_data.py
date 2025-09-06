# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["2975"],
        # Outputs
        ["Escribe un numero entero: ", "23"],
        # Message in case of failure
        "Debes sumar bien los dígitos de un número entero"
    ),
    # Test case 2
    (
        # Inputs
        ["15"],
        # Outputs
        ["Escribe un numero entero: ", "6"],
        # Message in case of failure
        "Debes sumar bien los dígitos de un número entero"
    ),
    # Test case 3
    (
        # Inputs
        ["-320"],
        # Outputs
        ["Escribe un numero entero: ", "5"],
        # Message in case of failure
        "Debes considerar que si la entrada es negativa, la salida es positiva"
    ),

]
