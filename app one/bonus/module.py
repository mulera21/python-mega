from parser import parse, convert

feet_inches = input("Enter feet and inches: ")
parsed = parse(feet_inches)

results = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {results}")

if results < 1:
    print("kids can slide")
else:
    print("too small")



