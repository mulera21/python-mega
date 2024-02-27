todos = []
while True:
    action = input('enter your vegetable you like: add, edit, show, exit')
    action= action.strip()
    match action:
        case 'add':
            todo = input('enter a veges')
            todos.append(todo)
        case 'show':
            for items in todos:
                print(items)
        case 'exit':
            break

        case 'edit':
            number = int(input('enter the veges number to edit'))
            number = number - 1
            new_todo = input('new veges')
            todos[number] = new_todo





