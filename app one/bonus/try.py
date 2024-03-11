try:
    width = float(input("enter the width"))
    length = float(input("enter the length"))
    if width == length:
        exit("looks like square")

    area = length * width

    print(area)
except ValueError:
    print("enter a  number")