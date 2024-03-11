todos = []
while True:
    user_action = input("enter a todo add, show, edit, complete or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo") + "\n"

            file = open("../app one/files/todo.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("../app one/files/todo.txt", "w")
            file.writelines(todos)
            file.close()

        case 'show':
            for i, j in enumerate(todos):
                row = f"{i + 1}-{j.capitalize()}"
                print(row)
        case 'edit':
            try:
                number = int(input("enter a number"))
                number = number - 1
                new_todo = input('enter a new todo')
                todos[number] = new_todo
            except ValueError:
                print("wrong command")
                new_todo = input('enter a new todo')
                todos[number] = new_todo

        case 'exit':
            break

        case 'complete':
            name = int(input('enter a number to remove'))
            todos.pop(name)
