# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["-10"],
            ["Introduce los grados: ", "excede"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["90"],
            ["Introduce los grados: ", "eje"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["45"],
            ["Introduce los grados: ", "cuadrante 1"],
            "Revisa tu código",
        ),
        # Test case 4
        (
            ["215"],
            ["Introduce los grados: ", "cuadrante 3"],
            "Revisa tu código",
        ),
    ]
