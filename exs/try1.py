"""

Coding Exercise 1
The given code is incomplete. Your task is to continue that program. You need to:
1. calculate the percentage using the  value/total * 100 formula
2. print out, for example, "That is 40.0%" as shown in the sample below:
The program should also print a message if the user doesn't enter a number
 for the "total value or for the "value":
"""

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    area = value/total_value * 100
    print(f"That is {area}%")
except ValueError:
    print("user does enter a number for the total value")
