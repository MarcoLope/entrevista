# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["1"],
        ["","1"],
        "Debe salir: 1"
    ),
    # Test case 2
    (
        ["3"],
        ["","1",  "2","3"],
        "Debe salir:'','1',  '2','3'"
    ),
# Test case 3
 (
    ["10"],
    ["",'1','2', '3','4','5','6','7','8','9','10'],
    "Debe salir: '','1','2', '3','4','5','6','7','8','9','10'"
),
# Test case 4
(
    ["11"],
    ["",'1','2', '3','4','5','6','7','8','9','10','11'],
    "Debe salir: '','1','2', '3','4','5','6','7','8','9','10','11'"
),
# Test case 5
(
    ["15"],
    ["",'1','2', '3','4','5','6','7','8','9','10','11','12','13','14','15'],
    "Debe salir: '','1','2', '3','4','5','6','7','8','9','10','11','12','13','14','15'"
)
]
