"""
Coding Exercise 2
We have a list of two IPs in the code area.
Extend the code so your program:
1. Prompts the user to input an index (e.g., 0 or 1).
2. Depending on the user input,
the program should return either
You chose 100.122.133.111 or You chose 100.122.133.111
Note: In order for the system to mark
 your exercise as correct, your code should
  return the exact output (i.e., upper case Y
  in You chose and no spaces or other characters
  after the IP.
"""
ips = ['100.122.133.105', '100.122.133.111']

index = int(input("Enter the index of the IP you wnat either 0 or 1"))

if 0 <= index < len(ips):
            print(f"You chose {ips[index]}.")