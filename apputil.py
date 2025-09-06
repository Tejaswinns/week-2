import numpy as np

#Exercise 1

def ways(num pennies,num nickels):

    """Return the number of ways to make change for num_pennies using a generator internally 
    returns: number of ways to make change"""

    # Generator function that yields all combinations of pennies and nickels

def gen()

    # try using 0 to num_nickels nickels

    for k in range(num_nickels + 1):

        # calculate remaining pennies after using k nickels

        remaining pennies = num_pennies - 5 * k

        # if remaining pennies is non-negative, yield 1 and recurse

        if remaining_pennies >= 0:

            yield 1 # yield 1 for this combination

            #count the total number of yields and return

            return sum(gen)

#Exercise 2

# Sample data
names = ['Alice', 'Bob', 'Charlie', 'David']

# Corresponding scores
scores = [85, 92, 78, 90]

# Convert to numpy arrays
np_names = np.array(names)
np_scores = np.array(scores)

#part 1

def lowest_score(names, scores):

    """Return the name with the lowest score"""

    scores_array = np.array(scores)

    # Find the index of the minimum score
    min_index = np.argmin(scores_array)

    # Return the corresponding name
    return names[min_index]

#part 2

def sort_names(names, scores):
    """Return names sorted by their corresponding scores in ascending order"""

    # Convert scores to a numpy array
    scores_array = np.array(scores)

    # Get the indices that would sort the scores
    sorted_indices = np.argsort(scores_array)

    # Use these indices to sort the names
    sorted_names = [names[i] for i in sorted_indices]

    return sorted_names