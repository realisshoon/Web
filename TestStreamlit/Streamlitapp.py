import streamlit as st
import pandas as pd

st.title('Ausra')

tab1,tab2,tab3= st.tabs(["intro","pick sound","community"])


with tab1:
     st.header("Welcome we are Asura")

with tab2:
     st.header("Choose the sound you want to detect")
     ##소리 선택
with tab3:
     st.write("질문을 등록해주세요")


