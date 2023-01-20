
while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"

            file = open('todos.txt', 'r')
            new_todos2 = file.readlines()
            file.close()

            print(new_todos2)
            new_todos2[number] = new_todo

            file = open('todos.txt', 'w')
            file.writelines(new_todos2)
            file.close()

        case 'delete':
            number = int(input("Number of the todo to delete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case other:
            print("You entered an unknown command.")

print("Bye!")





