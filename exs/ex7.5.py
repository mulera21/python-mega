"""
Extend the given code so it prints out the sum
of the numbers.
The output of your code should be as below:
49.1
"""
user_entries = ['10', '19.1', '20']

number = [float(num) for num in user_entries]

x = sum(number)
print(x)