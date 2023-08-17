import function
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("DarkGreen4")
clock = sg.Text('',key='clock')
label = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter Todo", key ='todo')
add_button = sg.Button('ADD')
list_box = sg.Listbox(values= function.get_todos(), key='item',
                      enable_events= True , size=[ 45,10])
edit_button = sg.Button('EDIT')
complete_button = sg.Button('COMPLETE')
exit_button = sg.Button('EXIT')
window =sg.Window('My To-Do App',
                  layout=[[clock],
                          [label],
                          [input_box,add_button],
                          [list_box, edit_button,complete_button],
                          [exit_button]]
                  ,font= ('arial',20))
while True:

    event, values = window.read(timeout= 10)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:M:%S"))
    print(1,event)
    print(2,values)
    print(3,values['item'])
    match event:
        case "ADD":
            todos = function.get_todos()
            new_todos = values['todo'] +"\n"
            todos.append(new_todos)
            function. write_todos(todos)
            window['item'].update(values=todos)
        case "EDIT":
            try:
                todo_to_edit = values['item'][0]
                new_todo = values['todo'] +"\n"
                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['item'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first")
        case "COMPLETE":
            try:
                todo_to_complete = values['item'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['item'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select an item first")
        case 'item':
            window['todo'].update(value=values['item'][0])
        case 'EXIT':
            break
        case sg.WIN_CLOSED:
            break
window.close()


window.close()

