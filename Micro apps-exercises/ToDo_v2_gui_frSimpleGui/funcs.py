import json
from itertools import count

FILEPATH = "todo.json"

def add_todos1(todos_msg):
    a = read_todos()
    task = {"Task": todos_msg, "Status": "ToDo"}
    a.append(task)
    with open(FILEPATH,'w') as file:
        file.write(json.dumps(a))

def write_todos(msg, FILEPATH:FILEPATH):
    with open(FILEPATH,'w') as file:
        file.write(json.dumps(msg))
    return read_todos()

def read_todos():
    try:
        with open(FILEPATH, 'r') as file:
            todos = json.load(file)
    except:
        return []
    return todos


def complete_todos1(idx):
    current = read_todos()
    try:
        idx=int(idx)
        idx = int(idx)
        if idx > 0:
            index_to_complete = idx
            current[index_to_complete]["Status"] = "Completed"
        else:
            index_to_complete = idx
            current[index_to_complete]["Status"] = "Completed"
        write_todos(current, FILEPATH)

    #     return f"Task No: {idx} marked as complete."
    except:
        pass



def delete_completed1():
    current = read_todos()
    a = [x for x in current if x["Status"] == "Completed"]
    [current.remove(x) for x in current if x["Status"] == "Completed"]
    new = [x for x in current if x["Status"] != "Completed"]
    write_todos(new, FILEPATH)
    # if a:
    #     write_todos(current, FILEPATH)

def delete_all():
    with open(FILEPATH,'w') as file:
        file.write(json.dumps([]))

def read_todos1():
    res = []
    try:
        with open(FILEPATH, 'r') as file:
            todos = json.load(file)
    except:
        return []
    result1 = [f"{x['Task']}:{x['Status']}" for x in todos]
    # result2 = [f"{x}:{y}" for x,y in enumerate(todos)]
    return result1
    # result = [f"Task: {todo['Task']}, status: {todo['Status']}+\n" for todo in todos]
    # res = [f"{x['Task']} with {x['Status']}" for x in todos]
    # print(res)
    # tod = todos[0]
    # result = '\n'.join([f"{key[0]}" for key, value in tod.items()])
    # return [',\n'.join(["A", "B", "C"])]


if __name__ == '__main__':
    pass
    # for x in read_todos():
    #     print(x['Task'])
    print(read_todos1())