# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:35:48 2022

@author: amber
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# session state variables
st.set_page_config(
    page_title= 'Multipage App')

st.header('Hier kunnen we een applicatie van maken')



st.session_state.upload_first_file = st.file_uploader('Upload Connexxion Data', accept_multiple_files=False , type='xlsx',)
st.session_state.upload_second_file = st.file_uploader('Upload Circulation Planning', accept_multiple_files=False , type='xlsx')


if st.session_state.upload_first_file and st.session_state.upload_second_file:
    st.markdown('---')
    df1 = pd.read_excel(st.session_state.upload_first_file, engine='openpyxl')
    df2 = pd.read_excel(st.session_state.upload_second_file, engine='openpyxl')
    st.dataframe(df1)
    st.dataframe(df2)


with st.form("Capaciteit bus"):
   st.write("tot hoeveel procent zijn de accus momenteel opgeladen?")
   st.session_state.percentage_opgeladen = st.slider('capaciteit bussen')
   percentage_opgeladen = st.form_submit_button("Submit")
   if st.session_state.percentage_opgeladen:
       st.write("opgeslagen")