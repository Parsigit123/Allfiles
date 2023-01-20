import PySimpleGUI as sg
from ZipCreator import make_archive, extract_archive


label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 =sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 =sg.FolderBrowse("Choose", key="folder")

compress_button =sg.Button("Compress")
output_label1 =sg.Text(key="output1", text_color="yellow")


label3 = sg.Text("Select files to Archive:     ")
input3 = sg.Input()
choose_button3 =sg.FileBrowse("Choose", key="archive")

label4 = sg.Text("Select destination folder: ")
input4 = sg.Input()
choose_button4 =sg.FolderBrowse("Choose", key="folder")

uncompress_button =sg.Button("Extract")
output_label2 =sg.Text(key="output2", text_color="yellow")

exit_button = sg.Button("Exit")

window = sg.Window('File Compressor/Uncompressor',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label1],
                           [label3, input3, choose_button3],
                           [label4, input4, choose_button4],
                           [uncompress_button, output_label2],
                           [exit_button]
                           ])


while True:
    event, values = window.read()
    print("--> Event:", event, "\n", "--> Values: ", values)
    match event:
        case "Compress":
            try:
                filepaths = values["files"].split(";")
                folder = values["folder"]
                make_archive(filepaths, folder)
                window["output1"].update(value="Compression completed!")
            except ValueError:
                sg.popup("Please provide files and destination folder!", font=("Helvetica", 15))

        case "Extract":
            try:
                dest_dir = values["folder"]
                archivepath = values["archive"]
                extract_archive(archivepath, dest_dir)
                window["output2"].update(value="Extracton completed!")
            except FileNotFoundError:
                sg.popup("Please provide zip file and destination folder!", font=("Helvetica", 15))

        case "Exit":
            break

        case sg.WIN_CLOSED:
             break

print("Bye!")
window.close()