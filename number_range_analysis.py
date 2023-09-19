#number_range_analysis.py
'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    # return sum(range(x,y +1))
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.

    return sum(range(start, end + 1))

def find_smallest_number(start, end):
    
    # return min(range(x, y + 1))
    
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.
    return min(range(start, end + 1))

def find_largest_number(start, end):
    
    # return max(range(x, y + 1))
    
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.
    return max(range(start, end + 1))

def count_even_numbers(start, end):
   
    # d = []
    # for i in range(a, b + 1):
    #   if i % 2 == 0:
    #       d.append(i)
    # return len(d)

    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
    even_numbers = []
    for number in range(start, end + 1):   
       if number % 2 == 0:
           even_numbers.append(number)
    return len(even_numbers)

def count_odd_numbers(start, end):
    
    # d = []
    # for i in range(a, b + 1):
    #   if i % 2 != 0:
    #       d.append(i)
    # return len(d)
    
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
    odd_numbers = []
    for number in range(start, end + 1):
       if number % 2 != 0:
           odd_numbers.append(number)
    return len(odd_numbers)