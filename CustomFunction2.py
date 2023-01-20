def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ write the to-do item list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


text = """
Principles of productivity.
Managing your inflow.
Systemizing everything that repeats.
"""

print(text)


while True:
    user_action = input("Type add activity, show, edit nr, delete nr or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
            todo = user_action[4:]

#            todos = get_todos("todos.txt")
#            todos = get_todos(filepath="todos.txt")
            todos = get_todos()

            todos.append(todo + '\n')

#            write_todos(todos, "todos.txt")
            write_todos(todos)


    elif user_action.startswith("show"):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

#            write_todos(todos, "todos.txt")
            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
#            user_action = input("Type add activity, show, edit nr, delete nr or exit: ")
#            user_action = user_action.strip()
            continue

    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])

            todos = get_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            print("(", todo_to_remove, ")", " was removed from the list.")

#            write_todos(todos, "todos.txt")
            write_todos(todos)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break


    else:
        print("You entered an unknown command.")

print("Bye!")

