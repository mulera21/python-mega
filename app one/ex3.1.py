todos = []

while True:
    user_action = input("type add, show or exit ")

    match user_action:
        case 'add':
            todo = input("enter a to do")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print('Bye!')
