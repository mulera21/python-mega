todos = []


while True:
    user_action = input("enter a todo add, show, edit, complete or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo")
            todos.append(todo)

        case 'show':
            for i, j in enumerate(todos):
                row = f"{i + 1}-{j.capitalize()}"
                print(row)
        case 'edit':
            number = int(input("enter a number"))
            number = number -1
            new_todo = input('enter a new todo')
            todos[number] = new_todo

        case 'exit':
            break

        case 'complete':
            name = int(input('enter a number to remove'))
            todos.pop(name)


