# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["1", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "30.48"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["2", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "2.54"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["-5", "1"],
            ["1. pies a cm, 2. pulgadas a cm, 3. yardas a cm", "Introduce una opcion: ", "Introduce la cantidad: ", "Error"],
            "Revisa tu código",
        ),
    ]
