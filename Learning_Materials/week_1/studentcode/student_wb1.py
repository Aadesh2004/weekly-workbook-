from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()
    
    # ====> insert your code below here
  # Loop through all possible values for digit1
    for digit1 in puzzle.value_set:
        # Loop through all possible values for digit2
        for digit2 in puzzle.value_set:
            # Loop through all possible values for digit3
            for digit3 in puzzle.value_set:
                # Loop through   all possible values for digit4
                for digit4 in puzzle.value_set:
                    # Set the values of the variables to the current combination
                    my_attempt.variable_values = [digit1, digit2, digit3, digit4]
                    try:
                        # Evaluate the puzzle using the current values
                        result = puzzle.evaluate(my_attempt.variable_values)
                        # If the result is 1 (correct solution), return the values
                        if result == 1:
                            return my_attempt.variable_values
                    except ValueError:
                        # If an invalid value is used, skip and try the next one
                        continue
    # <==== insert your code above here
    
    # should never get here
    return [-1, -1, -1, -1]

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    # Loop through each row in the namearray
    for row in range(namearray.shape[0]):
        # Get the last 6 characters from the current row (assumed to be the family name)
        family_name_array = namearray[row, -6:]
        # Join the characters into a single string
        family_name = ''.join(family_name_array)
        # Add the family name to the list
        family_names.append(family_name)
     
    
    # <==== insert your code above here
    return family_names

def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays
    
    # ====> insert your code below here
    # Check that the array is 9x9 in size (like a Sudoku grid)
    assert attempt.shape == (9, 9), "Array must be 9x9"

    # Add all 9 rows to the list called slices
    for i in range(9):
        slices.append(attempt[i, :])

    # Add all 9 columns to the slices list
    for j in range(9):
        slices.append(attempt[:, j])

    # Add all 9 sub-squares (3x3 blocks) to the slices list
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # Take a 3x3 block and flatten it into a 1D array
            slices.append(attempt[i:i+3, j:j+3].flatten())

    # Check each slice to see if it has 9 unique values
    for slice in slices:
        if len(np.unique(slice)) == 9:
            tests_passed += 1
    # <==== insert your code above here
    # return count of tests passed
    return tests_passed
