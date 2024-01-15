import streamlit as st
from inference import Medical_Inference

st.title(':red[       Medical Search Engine]')

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_input('Search Box', placeholder='Type your query here', max_chars=500)

with col2:
    select_model = st.selectbox('Select model', options=['Skipgram', 'Fasttext'])

submit_btn = st.button(label='predict', type='primary')
if submit_btn:
    Medical_Inference.process(input_text, select_model)