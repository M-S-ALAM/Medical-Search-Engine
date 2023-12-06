import streamlit as st


st.title('Medical Search Engine')


input_text = st.text_input('Search Box', placeholder='Type your query here', max_chars=500)
if input_text:
    st.write(input_text)