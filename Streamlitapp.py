import streamlit as st
import pandas as pd


title=st.title('Hello')
choices=st.multiselect('select your sound',["cat","dog"])
add_selectbox=st.sidebar.selectbox(
    "menu",
    ("Home","select sound")
)

if add_selectbox =="select sound":
    choices
else:
    print(title)