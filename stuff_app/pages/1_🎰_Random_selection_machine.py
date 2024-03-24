import cachetools
import streamlit as st

st.set_page_config(page_title="Random Selection Machine", page_icon=":slot_machine:")

st.sidebar.header("Random Selection Machine")

st.header("Random Selection Machine")

if 'elements' not in st.session_state:
    st.session_state.elements = []


box = st.container()

def adder():
    st.session_state.elements.append(st.session_state.element_to_add)



with box:
    element = st.chat_input("Enter the items to be picked here...", key='element_to_add', on_submit=adder)


print(st.session_state.elements)
for item in st.session_state.elements:
    st.sidebar.write(item)


