"""
Define a  water_state function that:
1. gets a temperature argument
2. returns the string "Solid" if the temperature is less than or equal to 0
3. returns "Liquid" if the temperature is greater than 0, but less than 100.
4. returns "Gas" if the temperature is greater than or equal to 100.
"""


def water_state(temperature):

    BOILING_POINT = 100
    FREEZING_POINT = 0

    if temperature <= FREEZING_POINT:
        return "Solid"

    elif temperature < BOILING_POINT:
        return "Liquid"

    else:
        return "Gas"
