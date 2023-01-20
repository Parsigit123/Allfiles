import PySimpleGUI as sg
from ZipCreator import extract_archive


label1 = sg.Text("Select files to Archive:     ")
input1 = sg.Input()
choose_button1 =sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 =sg.FolderBrowse("Choose", key="folder")

uncompress_button =sg.Button("Uncompress")
output_label1 =sg.Text(key="output1", text_color="yellow")

window = sg.Window('File Compressor/Uncompressor',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [uncompress_button, output_label1]])


while True:
    # event, values = window.read()
    # print("--> Event:", event, "\n", "--> Values: ", values)
    # filepaths = values["files"].split(";")
    # folder = values["folder"]
    # make_archive(filepaths, folder)
    # window["output1"].update(value="Compression completed!")

    event, values = window.read()
    print("--> Event:", event, "\n", "--> Values: ", values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output1"].update(value="Extracton completed!")


window.read()
window.close()