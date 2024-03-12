"""
Coding Exercise 2
Your task for this exercise is to complete the strength function.
The function is supposed to check the strength of the user's password.
The function should:
1. get a password argument
2. return the string "Strong Password" if all of the following conditions are true:
Eight or more characters
At least one uppercase letter.
At least one digit.
3. returns "Weak Password" if at least one of the three conditions is not met.
Note:  You can make use of the code we developed in the Bonus Example on Day 9.
"""


def strength(Password):
    number = 8
    if len(Password) < 8:
        return "weak password"

    has_uppercase = any(char.isupper() for char in Password)
    has_digit = any(char.isdigit() for char in Password)

    if has_digit and has_uppercase:
        return "strong Password"

    return "weak password"


action = input("password")

results = strength(action)
print(results)
