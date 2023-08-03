import streamlit as st
import functions as fn

todos = fn.get_data()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"

    is_taken = False
    for todo in todos:
        if new_todo == todo:
            print("taken")
            is_taken = True
            st.session_state["new_todo"] = "Todo is taken"
            break

    if len(new_todo) > 0 and is_taken == False and st.session_state["new_todo"] != "Todo is taken":
        todos.append(new_todo)
        fn.write_data(todos)
        st.session_state["new_todo"] = ""

st.title("My first python web app")
st.subheader("This is the famous todo app 🎇")
st.write("You can add your todos and remove")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_data(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label="Enter a todo:", placeholder="",
              on_change=add_todo, key="new_todo")

# st.session_state
