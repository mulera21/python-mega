"""
Coding Exercise 2
Create a program that prompts the user to input
their name once. Then, the program repeatedly
prints out the name with the first letter capitalized.
"""

user_prompt = "enter your name"
while True:
    todo = input(user_prompt)
    print(todo.capitalize())

