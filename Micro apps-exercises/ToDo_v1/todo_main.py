import json
import funcs
import os
from json import JSONDecodeError
from pprint import pprint

if not os.path.exists(funcs.FILEPATH):
    with open("todo.txt", "w") as file:
        pass


#
commands = {"Add": funcs.write_todos, "Show": funcs.read_todos, "Change": funcs.edit_todos, "Complete": funcs.complete_todos}
todo_list = []

while True:
    todo_command = input(f"Hello. Please type your command: {', '.join([x for x in commands])}: ")

    if todo_command.startswith("Add"):
        task = todo_command[4:]
        current_todos = funcs.read_todos()
        current_todos.append(task+'\n')
        funcs.write_todos(current_todos)
        print(f"{task} was added successfully")
    elif  todo_command.startswith("Show"):
        for idx, content  in enumerate(funcs.read_todos()):
            print(f"Task No {idx+1}: {content}".strip('\n'))
    elif todo_command.startswith("Change"):
        print(funcs.edit_todos(todo_command))
    elif todo_command.startswith("Complete"):
        print(funcs.complete_todos(todo_command))

    elif todo_command == "Exit":

        break




