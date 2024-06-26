import streamlit as st
import experimentIf

result = experimentIf.get_variables()

def add_variable():
    variable = st.session_state["new_variable"]
    result.append(variable.title() + "\n")
    experimentIf.ouput_variables(result)

st.title("My List App")
st.subheader("This is an app for lists.")
st.write("This app is to increase your productivity.")

for index, variable in enumerate(result):
    checkbox = st.checkbox(variable, key=variable)
    if checkbox:
        result.pop(index)
        experimentIf.ouput_variables(result)
        del st.session_state[variable]
        st.rerun()

st.text_input(label="", placeholder="Enter an item... ",
              on_change=add_variable, key='new_variable')
