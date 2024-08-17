
FILEPATH = "todo.txt"

def write_todos(todo_msg):
    with open(FILEPATH,'w') as file:
        file.writelines(todo_msg)
    return read_todos()

def read_todos():
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
        return todos

def edit_todos(change_command):
    current = read_todos()
    try:
        com, idx, new_content = change_command.split(" ")

        idx = int(idx)
        if idx > 0:
            current[idx - 1] = new_content +'\n'
        else:
            current[idx] = new_content + '\n'
        write_todos(current)
        return f"Successfully changed the task to: {new_content}."
    except:

        return ("Please try again with valid index/content")


def complete_todos(change_command):
    current = read_todos()
    try:
        com, idx = change_command.split(" ")
        idx = int(idx)
        if idx > 0:
            index_to_remove = idx -1
            current.pop(index_to_remove)
        else:
            index_to_remove = idx
            current.pop(index_to_remove)
        write_todos(current)
        return f"Successfully completed task No: {idx}."
    except:
        return ("Please try again with valid index")

if __name__ == '__main__':
    write_todos("asddasd")

