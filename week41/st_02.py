import streamlit as st
import time

st.title('VÍ DỤ CÁC WIDGETS')

total = 0
if st.button('Hello World'):
    st.write('Hello from Streamlit!')

if st.checkbox('Apple ($2)'):
    total += 2

if st.checkbox('Banana ($1.5)'):
    total += 1.5

if st.checkbox('Cherry ($3)'):
    total += 3

st.write(f'Total: ${total}')

gender = st.radio('Select your gender', ['Male', 'Female', 'Other'], index=2)
st.write(f'You are {gender}')

languages = st.selectbox('Languages', ['English', 'Vietnamese', 'French'], index=1)
st.write(f'You speak {languages}')

prog_languages = st.multiselect('Programming Languages', ['Python', 'Java', 'C++', 'C#', 'JavaScript'], default=['Python', 'Java'])
st.write(f'You know {', '.join(prog_languages)}')

number = st.slider('Number', min_value=0, max_value=100, value=25)
st.write(f'You selected {number}')

bar = st.progress(0)
for i in range(1, 100):
    bar.progress(i)
    time.sleep(0.1)


with st.spinner('Waiting for data...'):
    time.sleep(3)
    st.write('Data loaded')
