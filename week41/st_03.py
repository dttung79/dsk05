import streamlit as st

st.set_page_config(layout='wide')
with st.container():
    st.title('Banner of the website')

st.sidebar.title('Menu')
choice = st.sidebar.selectbox('Select a page', ['Home', 'About', 'Contact'])

with st.container():
    if choice == 'Home':
        st.write('This is the content of the home page')
    elif choice == 'About':
        st.write('This is the content of the about page')
    elif choice == 'Contact':
        st.write('This is the content of the contact page')