import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")


def load_data():
    st.header("Tải Dữ Liệu Thuê Xe Đạp")
    day_col, hour_col = st.columns(2)
    with day_col:
        day_file = st.file_uploader("Tải lên tệp CSV cho dữ liệu hàng ngày", type=["csv"])
        
    with hour_col:
        hour_file = st.file_uploader("Tải lên tệp CSV cho dữ liệu hàng giờ", type=["csv"])
    
    if day_file is not None and hour_file is not None:
        day_data = load_day_csv(day_file)
        hour_data = load_hour_csv(hour_file)
        
        st.subheader("Dữ liệu thuê xe đạp hàng ngày")
        st.dataframe(day_data.head())
        
        st.subheader("Dữ liệu thuê xe đạp hàng giờ")
        st.dataframe(hour_data.head())
        
        st.success("Dữ liệu đã được tải thành công!")

@st.cache_data
def load_day_csv(day_file):
    return pd.read_csv(day_file)

@st.cache_data
def load_hour_csv(hour_file):
    return pd.read_csv(hour_file)
    
def plot_correlation_matrix():
    st.header("Ma trận tương quan của dữ liệu thuê xe đạp hàng ngày")

def plot_bar_chart():
    st.header("Biểu đồ cột của dữ liệu thuê xe đạp hàng ngày")

def plot_line_chart():
    st.header("Biểu đồ đường của dữ liệu thuê xe đạp hàng giờ")