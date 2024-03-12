"""
Coding Exercise 3
Define a function that takes a list as an argument and returns
the average value of the list items. For example,
if I called your function with foo([10, 20, 30, 40])
 it should return 25, the average of the numbers of the list.
"""


def calculate_average(items):
    """Calculates the average of a list of numbers.

    Args:
        items: A list of numbers.

    Returns:
        The average (mean) of the numbers in the list.
    """

    if not items:  # Check for empty list
        return None

    total = sum(items)
    average = total / len(items)
    return average

# Example usage with a list provided as an argument
item_list = [17, 56, 67, 65]
average_result = calculate_average(item_list)
print(average_result)
