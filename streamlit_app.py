import streamlit as st

conn = st.experimental_connection('pet_db', type='sql')
students = conn.query('select * from student')
st.dataframe(students)