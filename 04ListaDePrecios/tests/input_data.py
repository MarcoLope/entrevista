# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        ["A", "X"],
        ["Teclea la clave ", "120","Teclea la clave ", "120"],
        ["Revisa la clave A."]
    ),
    # Test case 2
    (
        ["C","B","X"],
        ["Teclea la clave ", "360", "Teclea la clave ", "250", "Teclea la clave ", "610"],
        ["Revisa la clave B y C y que la suma sea correcta."]
    ),
    # Test case 3
    (
        ["X"],
        ["Teclea la clave ", "0"],
        ["Revisa el caso de que el usuario no quiera comprar nada."]
    )
]