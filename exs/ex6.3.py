"""
Write a program that reads the essay.
txt file and returnsthe number of characters
contained in the file.
"""
file = open("nice.txt", "r")
data = file.read()
number = len(data)
print(number)