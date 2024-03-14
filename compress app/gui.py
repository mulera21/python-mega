import PySimpleGUI as sg

label1 = sg.Text("select file to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("choose", key="file")

label2 = sg.Text("select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose", key="folder")
compress_button = sg.Button("compress")
window = sg.Window("FILE COMPRESSOR",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["file"].split(";")
    folder = values["folder"]
window.close()