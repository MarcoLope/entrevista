# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["10","20","-1"],
    ["","","", "15.0"],
    ["El promedio no es correcto. ¿Consideraste que no debes sumar el número negativo?"]
    ),
    # Test case 2
    (
    ["2","8","14","-1"],
    ["","","","", "8.0"],
    ["El promedio no es correcto. ¿Consideraste que no debes sumar el número negativo?"]
    ),
    # Test case 3
    (
    ["5.4","6.1","4.28","3.179", "-10"],
    ["","","","","", "4.73975"],
    ["El promedio no es correcto. ¿Consideraste que no debes sumar el número negativo? ¿Consideraste números flotantes?"]
    )
]
