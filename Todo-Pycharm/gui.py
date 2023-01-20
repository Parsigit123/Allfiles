import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists(("todos.txt")):
    with open("todos.txt", "w") as file:
        pass


#sg.theme("DarkTeal12")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo:", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")

list_box =sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
#delete_button = sg.Button("Delete")
delete_button = sg.Button(size=2, image_source="delete.png", mouseover_colors="LightBlue2",
                       tooltip="Delete Todo", key="Delete")
exit_button = sg.Button("Exit")
#output_label =sg.Text(key="output", text_color="yellow")

# layout = [[label],
#           [input_box, add_button],
#           [list_box, edit_button, delete_button],
#           [exit_button, output_label]]

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, delete_button],
          [exit_button]]


window = sg.Window('My To-Do App', layout=layout, font=("Helevetica", 15))

while True:
    event, values = window.read(timeout=20)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M"))
    # print(" --> Event: ", event)
    # print(" --> Values: ", values)
    # print(" --> Values todos: ", values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                print("Please select an item first!")
#                window["output"].update(value="Please select an item first!")
                sg.popup("Please select an item first!", font=("Helevetica", 15))
        case "Delete":
            try:
                todo_to_delete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=("Helevetica", 15))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
#           exit()
            break
print("Bye!")
window.close()