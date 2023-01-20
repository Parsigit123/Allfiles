user_promt = "Enter a todo: "

todos = []
todo = ""

while todo != "0":
    todo = input(user_promt)
    todos.append(todo)
    print("Your answers are: ", todos)
print("Finished.")