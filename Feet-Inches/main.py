import PySimpleGUI as sg
from converters import convert

print("This program converts feet/inches to meters.")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert", key="Convert")
output_label = sg.Text(key="output")

exit_button = sg.Button("Exit")

col1 = sg.Column([[feet_label], [inches_label]])
col2 = sg.Column([[feet_input], [inches_input]])

window = sg.Window("Convertor", layout=[[col1, col2], [button], [exit_button, output_label]])

# while True:
#     event, values = window.read()
#     match event:
#         case "Convert":
#             feet = float(values["feet"])
#             inches = float(values["inches"])
#             result = convert(feet, inches)
#             window["output"].update(value=f"{result} m", text_color="yellow")
#         case "Exit":
#             break
#         case sg.WIN_CLOSED:
#             break

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="yellow")
    except ValueError:
        sg.popup("Please provide two numbers.", font=("Helvetica", 15))

window.close()