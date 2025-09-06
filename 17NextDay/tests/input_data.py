# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple


input_values = [
    # Test case 1
    (
        ["28", "2", "2020"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 29/2/2020"],
        'Error',
    ),
    # Test case 2
    (
        ["28", "2", "2024"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 29/2/2024"],
        'Error',
    ),
    # Test case 3
    (
        ["28", "2", "2022"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 1/3/2022"],
        'Error',
    ),
    # Test case 4
    (
        ["31", "12", "2022"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 1/1/2023"],
        'Error',
    ),
    # Test case 5
    (
        ["30", "12", "2022"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 31/12/2022"],
        'Error',
    ),
    # Test case 6
    (
        ["31", "5", "2022"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 1/6/2022"],
        'Error',
    ),
    # Test case 7
    (
        ["5", "8", "2022"],
        ["Enter the day: ", "Enter the month: ",
         "Enter the year: ", "Next day: 6/8/2022"],
        'Error',
    ),
]
