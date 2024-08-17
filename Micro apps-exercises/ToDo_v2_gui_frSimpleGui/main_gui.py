import os

import FreeSimpleGUI as sg
import funcs
import time
# add_todos
# read_todos

MIN_LEN = 5

files_btn = sg.Button("Add")
fldr_btn = sg.Button("Add")

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")

listbox = sg.Listbox(values=[f'{x}: {y}' for x, y in enumerate(funcs.read_todos1())],
                     key="todos",
                     enable_events=True,
                     size=(25,10))
complete_button = sg.Button("Complete")
add_button = sg.Button("Add")
del_button = sg.Button("Delete completed")
del_all_button = sg.Button("Delete ALL")
eject_button = sg.Button("Eject")
window = sg.Window("To-do manager",
                   layout=[[label],[input_box, add_button], [listbox, complete_button], [del_button, del_all_button, eject_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read()
    # print(event)
    if event == "Add":

        todo_to_add = values['todo']
        if len(todo_to_add) <= MIN_LEN:
            input_box.update("Min 5")
        else:
            funcs.add_todos1(todo_to_add)
            window['todos'].update(values=[f'{x}: {y}' for x, y in enumerate(funcs.read_todos1())])
            input_box.update("")
    elif event == "Complete":
        try:
            todo_for_edit=values['todos'][0].split(":")[1]
            index = values['todos'][0].split(":")[0]
            funcs.complete_todos1(index)
            window['todos'].update(values=[f'{x}: {y}' for x, y in enumerate(funcs.read_todos1())])
        except IndexError:
            pass

        window['todos'].update(values=[f'{x}: {y}' for x, y in enumerate(funcs.read_todos1())])
    elif event == "Delete completed":
        funcs.delete_completed1()
        window['todos'].update(values=[f'{x}: {y}' for x, y in enumerate(funcs.read_todos1())])
    elif event == "Delete ALL":
        funcs.delete_all()
        window['todos'].update(values=[f'{x}: {y}' for x, y in enumerate(funcs.read_todos1())])
    elif event == "Eject":
        input_box.update("Nope :)")


    if event == sg.WIN_CLOSED:
        break


window.close()

if __name__ == "__main__":
    a = funcs.read_todos()
    print(a)