import function
import PySimpleGUI as sg
label = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter Todo", key ='todo')
add_button = sg.Button("ADD")

window =sg.Window('My To-Do App',
                  layout=[[label],[input_box,add_button]]
                  ,font= ('arial',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "ADD":
            todos = function.get_todos()
            new_todos = values['todo'] +"\n"
            todos.append(new_todos)
            function. write_todos(todos)

        case sg.WIN_CLOSED:
            break
window.close()


window.close()

