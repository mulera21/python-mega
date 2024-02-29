todos = []
# complete todo
while True:
    user_action = input("type add, edit,show,complete or exit ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a to do")
            todos.append(todo)
        case 'show':
            for index, items in enumerate(todos):
                row = f"{index + 1}-{items}"
                print(row)

        case 'complete':
            number = int(input('enter a number to complete'))
            todos.pop(number - 1)

        case 'exit':
            break
        case 'edit':
            number = int(input('enter a number'))
            number = number - 1
            new_todo = input('enter new todo')
            todos[number] = new_todo
print('Bye!')
