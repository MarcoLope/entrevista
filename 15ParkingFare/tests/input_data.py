# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["0", "0"],
            ["Enter number of hours: ", "Enter number of minutes: ", '0'],
            'Pay $0 if there is no time',
        ),
        # Test case 2
        (
            ["0", "10"],
            ["Enter number of hours: ", "Enter number of minutes: ", '5'],
            'Pay $5 for the first 2 hours',
        ),
        # Test case 3
        (
            ["1", "40"],
            ["Enter number of hours: ", "Enter number of minutes: ", '5'],
            'Pay $5 for the first 2 hours',
        ),
        # Test case 4
        (
            ["2", "30"],
            ["Enter number of hours: ", "Enter number of minutes: ", '17'],
            'During the third hour, pay $ 5 + 12',
        ),
        # Test case 5
        (
            ["3", "1"],
            ["Enter number of hours: ", "Enter number of minutes: ", '22'],
            'For 3:01, pay $ 5 + 12 + 5',
        ),
        # Test case 6
        (
            ["3", "20"],
            ["Enter number of hours: ", "Enter number of minutes: ", '25'],
            'For 3:20, pay $ 5 + 12 + 5 + 3',
        ),
        # Test case 7
        (
            ["4", "31"],
            ["Enter number of hours: ", "Enter number of minutes: ", '39'],
            'For 4:31, pay $ 5 + 12 + 12 + 5 + 3 + 2',
        ),
        # Test case 8
        (
            ["6", "50"],
            ["Enter number of hours: ", "Enter number of minutes: ", '65'],
            'For 6:50, pay $ 5 + 12 + 12 + 12 + 12 + 5 + 3 + 2 + 2',
        ),
    ]
