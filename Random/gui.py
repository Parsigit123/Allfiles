import PySimpleGUI as sg
import random


label1 = sg.Text("Lower band: ")
input_box1 = sg.InputText(tooltip="Enter the lower band", key="dig1")

label2 = sg.Text("Upper band: ")
input_box2 = sg.InputText(tooltip="Enter the upper band", key="dig2")

cr_button = sg.Button("Create Random")

output = sg.Text(key="output", text_color="yellow")

window = sg.Window('Random digit creator',
                   layout=[[label1, input_box1],
                           [label2, input_box2],
                           [cr_button, output]], font=('Helvetica', 15))


while True:
    event, values = window.read()
    match event:
        case "Create Random":
            dig1 = float(values["dig1"])
            dig2 = float(values["dig2"])
            rand = random.randint(dig1, dig2)
            print(rand)
            window['output'].update(value=rand)
        case sg.WIN_CLOSED:
            break

window.read()
window.close()
