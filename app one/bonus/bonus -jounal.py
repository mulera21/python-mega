date = input("enter to day's date:")
mood = input("how do you rate your mood 1 to 10")
thoughts = input("let you thought flow:\n")

with open(f"../files/{date}.txt", "w") as file:
    file.write(mood)
    file.write(thoughts)
