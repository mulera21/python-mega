FILEPATH = "home.txt"


def get_todos(filepath=FILEPATH):
    """
    read text file and return a list of todos
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath= FILEPATH):
    """
    write todos list in text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())



