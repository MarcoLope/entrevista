# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["a", "p"],
            ["Tirada de Ana: ", "Tirada de Juan: ", "Gana Juan"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["t", "p"],
            ["Tirada de Ana: ", "Tirada de Juan: ", "Gana Ana"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["a", "a"],
            ["Tirada de Ana: ", "Tirada de Juan: ", "Empate"],
            "Revisa tu código",
        ),
        # Test case 4
        (
            ["piedra", "a"],
            ["Tirada de Ana: ", "Tirada de Juan: ", "Las tiradas deben ser un caracter"],
            "Revisa tu código",
        ),
        # Test case 5
        (
            ["p", "r"],
            ["Tirada de Ana: ", "Tirada de Juan: ", "Tirada incorrecta"],
            "Revisa tu código",
        ),
    ]
