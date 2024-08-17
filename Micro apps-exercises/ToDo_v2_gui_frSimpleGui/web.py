import copy
import streamlit as st
import funcs


todos = funcs.read_todos()

def add_to_do():
    todo = st.session_state["new_todo"]
    funcs.add_todos(todo)

st.title("Some title")
st.subheader("Todo apprrrrrrer")
st.write("Some other")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new task", on_change=add_to_do, key="new_todo")
