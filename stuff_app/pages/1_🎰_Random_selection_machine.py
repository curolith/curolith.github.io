import random

import cachetools
import streamlit as st
import pyperclip

st.set_page_config(page_title="Random Selection Machine", page_icon=":slot_machine:")

st.sidebar.header("Item pool")

st.header("Random Selection Machine")

if 'elements' not in st.session_state:
    st.session_state.elements = []

if 'selection' not in st.session_state:
    st.session_state.selection = None

if 'remover_active' not in st.session_state:
    st.session_state.remover_active = 0

if 'distribution' not in st.session_state:
    st.session_state.distribution = []

if 'key_gen' not in st.session_state:
    st.session_state.key_gen = 0

if 'remaining' not in st.session_state:
    st.session_state.remaining = []

box = st.container()

st.session_state.selection = None


def key_gen():
    i = st.session_state.key_gen
    st.session_state.key_gen = i+1
    return f'generated_key_{i}'

def adder():
    st.session_state.elements.append(st.session_state.element_to_add)

def selecter(item):
    if st.session_state.remover_active == 1:
        st.session_state.selection = item


def toggle_remover():
    st.session_state.remover_active = st.session_state.remover_active + 1


def even_dist(n, i):
    elements = st.session_state.elements.copy()
    boxes = [[] for i in range(0, n)]
    print(boxes)
    c_box = 0
    while len(elements) > 0 and len(boxes[c_box]) < i:
        print(len(elements), len(boxes[c_box]), print(c_box))
        boxes[c_box].append(elements.pop(random.randint(0, len(elements)-1)))
        if c_box == n-1:
            c_box = 0
        else:
            c_box = c_box+1
    st.session_state.distribution = boxes
    if len(elements) > 0:
        st.session_state.remaining = elements
    else:
        st.session_state.remaining = []


def fill(n, i):
    elements = st.session_state.elements.copy()
    boxes = [[] for j in range(0, n)]
    print(boxes)
    c_box = 0
    while len(elements) > 0 and c_box < n:
        print(len(elements), len(boxes[c_box]), print(c_box))
        boxes[c_box].append(elements.pop(random.randint(0, len(elements) - 1)))

        if len(boxes[c_box]) == i:
            c_box = c_box + 1

    st.session_state.distribution = boxes
    if len(elements) > 0:
        st.session_state.remaining = elements
    else:
        st.session_state.remaining = []




def random_selection(n, i, d):
    if len(st.session_state.elements) < 1:
        return
    if d:
        even_dist(n, i)
    else:
        fill(n, i)









with box:
    element = st.chat_input("Enter the items to be picked here...", key='element_to_add', on_submit=adder)


print(st.session_state.elements)

for item in st.session_state.elements:
    st.sidebar.button(item, on_click=selecter(str(item)), type='secondary', key=key_gen())

# if len(st.session_state.elements) > 0:
#     st.sidebar.divider()
#     st.sidebar.button("Remove elements", type='secondary', on_click=toggle_remover)

with st.container():
    with st.popover("Configuration"):
        col1, col2, col3 = st.columns(3)

        with col1:
            n_elements = st.number_input("Number of groups", step=1, min_value=1, value=1)

        with col2:
            i_size = st.number_input("Group size", step=1, min_value=1, value=1)

        with col3:
            d_even_dist = st.toggle("Distribute evenly")
    st.button("Randomize", on_click=random_selection(n_elements, i_size, d_even_dist), type='primary')

print(n_elements, i_size, d_even_dist)

if len(st.session_state.distribution) > 0:
    st.divider()

with st.container():

    tripple_dist = [[],[],[]]

    boxes = st.session_state.distribution.copy()

    iter_index = 0
    counter = 1
    remaining_set = False
    while len(boxes) != 0 or not remaining_set:
        if len(boxes) == 0:
            remaining_set = True
            if len(st.session_state.remaining) > 0:
                tripple_dist[iter_index].append(['Remaining', st.session_state.remaining])
        else:
            tripple_dist[iter_index].append([f"Group {counter}", boxes.pop(0)])
            counter = counter+1
            if iter_index == 2:
                iter_index = 0
            else:
                iter_index = iter_index+1


    left, center, right = st.columns(3)

    with left:
        for element_map in tripple_dist[0]:
            with st.container():
                st.write(element_map[0])
                for elitem in element_map[1]:
                    st.button(elitem, key=key_gen())


    with center:
        for element_map in tripple_dist[1]:
            with st.container():
                st.write(element_map[0])
                for elitem in element_map[1]:
                    st.button(elitem, key=key_gen())


    with right:
        for element_map in tripple_dist[2]:
            with st.container():
                st.write(element_map[0])
                for elitem in element_map[1]:
                    st.button(elitem, key=key_gen())



if len(st.session_state.distribution) > 0:
    st.divider()
    st.write("Click the icon on the right to copy the selection:")
    st.code(st.session_state.distribution + st.session_state.remaining)



