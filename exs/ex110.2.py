"""
Define a function that:
(1) takes a temperature as a parameter
(2) returns "Hot" if the temperature is greater than 25
(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
(4) returns "Cold" if the temperature is less than 15.
If I called your function with foo(10) it would return "Cold".
foo(15) or foo(16) or foo(25) would all return "Warm" and foo(26) would return "Hot".
"""


def home(temp):
    hiegest = 25
    low = 15
    if temp < low:
        return "Cold"
    elif temp > hiegest:
        return "Hot"

    else:
        return "Warm"