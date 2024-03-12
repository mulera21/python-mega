"""
Coding Exercise 2
Write a get_nr_items function that:
1.gets as a parameter one string with commas. E.g., "john,lisa, teresa"
2. the function should return the number of items
divided by commas in that string (i.e., that would be three items in
 the above example)
2. returns the number of items.
"""


def get_nr_items(string_with_commas):
    number_of_items = len(string_with_commas.split(","))
    return number_of_items


string = "john,lisa,teresa"
number_of_items = get_nr_items(string)
print(number_of_items)
