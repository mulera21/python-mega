feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters  # decapoling


parsed = parse(feet_inches)

results = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {results}")

if results < 1:
    print("kids can slide")
else:
    print("too small")



