import streamlit as st

conn = st.experimental_connection('streamlit', type='sql')
students = conn.query('select * from student')
st.dataframe(students)