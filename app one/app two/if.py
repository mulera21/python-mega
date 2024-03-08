
while True:
    user_action = input("enter a todo add, show, edit, complete or exit")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]  # indexing where to start

        with open("home.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("home.txt", "w") as file:
            file.writelines(todos)

    if 'show' in user_action:
        for i, j in enumerate(todos):
            row = f"{i + 1}-{j.capitalize()}"
            print(row)
    if 'edit' in user_action:
        number = int(input("enter a number"))
        number = number - 1
        new_todo = input('enter a new todo')
        todos[number] = new_todo

    if 'exit' in user_action:
        break

    if 'complete' in user_action:
        name = int(input('enter a number to remove'))
        todos.pop(name)

