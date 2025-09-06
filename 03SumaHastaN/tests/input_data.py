# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        #Inputs
        ["9"],
        # Ouputs
        ["", "45"],
        # Message in case of failure
        ["La suma no es correcta."]
    ),
    # Test case 2
    (
        #Inputs
        ["155"],
        # Ouputs
        ["", "12090"],
        # Message in case of failure
        ["La suma no es correcta."]
    ),
    # Test case 3
    (
        #Inputs
        ["12090"],
        # Ouputs
        ["", "73090095"],
        # Message in case of failure
        ["La suma no es correcta."]
    ),
    # Test case 4
    (
        #Inputs
        ["0"],
        # Ouputs
        ["", "0"],
        # Message in case of failure
        ["¿Consideraste el caso de que el input sea 0?"]
    )
    
]
