def get_home():
    with open("../files/data.txt", "r") as file:
        data = file.readlines()
    value = data[1:]
    values = [float(i) for i in value]

    avarage_local = sum(values) / len(values)
    return avarage_local


sam = get_home()
print(sam)
