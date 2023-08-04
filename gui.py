import function
import PySimpleGUI as sg
label = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter Todo")
add_button = sg.Button("ADD")

window =sg.Window('My To-Do App',layout=[[label],[input_box,add_button]])
window.read()
window.close()

