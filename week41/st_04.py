import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_histogram():
    numbers = np.random.normal(0, 1, 100)
    fig, ax = plt.subplots()
    ax.hist(numbers, bins=20)
    st.pyplot(fig)

def show_bar_chart():
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [90, 20, 30, 80, 50]
    })
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Value'])
    st.pyplot(fig)

def show_line_chart():
    st.write('Line Chart under development')

def show_pie_chart():
    st.write('Pie Chart under development')

# Main webpage
st.title('Demo Charts')

st.sidebar.title('Select a chart')
chart_type = st.sidebar.selectbox('Select a chart', ['Histogram', 'Bar Chart', 'Line Chart', 'Pie Chart'])

if chart_type == 'Histogram':
    show_histogram()
elif chart_type == 'Bar Chart':
    show_bar_chart()
elif chart_type == 'Line Chart':
    show_line_chart()
elif chart_type == 'Pie Chart':
    show_pie_chart()