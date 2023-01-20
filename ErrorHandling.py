
while True:
    user_action = input("Type add activity, show, edit nr, delete nr or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
            todo = user_action[4:]

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')
            print(todos)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

    elif user_action.startswith("show"):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
#            user_action = input("Type add activity, show, edit nr, delete nr or exit: ")
#            user_action = user_action.strip()
            continue

    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            print("(", todo_to_remove, ")", " was removed from the list.")

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break


    else:
        print("You entered an unknown command.")

print("Bye!")





