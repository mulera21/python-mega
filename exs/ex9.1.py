"""
Coding Exercise 1
Create a liters_to_m3 function that:
1. gets a liters parameter
2. converts liters to cubic meters knowing
that 1000 liters are equal to 1 cubic meter and returns the cubic meters.
Note: Defining the function is enough.
You do not need to call or print out a function output,
but you should name the function exactly liters_to_m3.
"""


def liters_to_m3(liters):
    conversion = 1000
    cubic_meters = liters / conversion
    return cubic_meters

