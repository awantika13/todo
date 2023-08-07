import function
import PySimpleGUI as sg
label = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter Todo", key ='todo')
add_button = sg.Button("ADD")
list_box = sg.Listbox(values= function.get_todos(), key='item',
                      enable_events= True , size=[ 45,10])
edit_button = sg.Button('EDIT')
window =sg.Window('My To-Do App',
                  layout=[[label],[input_box,add_button],[list_box, edit_button]]
                  ,font= ('arial',20))
while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(values['item'])
    match event:
        case "ADD":
            todos = function.get_todos()
            new_todos = values['todo'] +"\n"
            todos.append(new_todos)
            function. write_todos(todos)
        case "EDIT":
            todo_to_edit = values['item'][0]
            new_todo = values['todo']
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['item'].update(values=todos)
        case 'item':
            window['todo'].update(value= values['item'][0])
        case sg.WIN_CLOSED:
            break
window.close()


window.close()

