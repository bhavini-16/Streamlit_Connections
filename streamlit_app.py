import streamlit as st
from datetime import timedelta
from sqlalchemy import text  # Import text from sqlalchemy

# Establish a connection to the MySQL database using the correct connection name
conn = st.experimental_connection('streamlit', type='sql')

with conn.session as s:
    st.markdown(f"Note that `s` is a `{type(s)}`")
    s.execute(text('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);'))  # Use text() for SQL statement
    s.execute(text('DELETE FROM pet_owners;'))  # Use text() for SQL statement
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),  # Use text() for SQL statement
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

pet_owners = conn.query('SELECT * FROM pet_owners', ttl=timedelta(minutes=10))
st.dataframe(pet_owners)
