import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
from bike_utils import load_data, plot_correlation_matrix, plot_bar_chart, plot_line_chart

# Cấu hình trang
st.set_page_config(
    page_title="Phân Tích Dữ Liệu Thuê Xe Đạp",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🚲 Phân Tích Dữ Liệu Thuê Xe Đạp")

st.sidebar.title("Lựa Chọn Tác Vụ")

task = st.sidebar.selectbox(
    "Chọn tác vụ bạn muốn thực hiện:",
    [
        "Tải Dữ Liệu",
        "Vẽ Ma trận tương quan",
        "Vẽ biểu đồ cột",
        "Vẽ biểu đồ đường"
    ]
)

if task == "Tải Dữ Liệu":
    load_data()
elif task == "Vẽ Ma trận tương quan":
    plot_correlation_matrix()
elif task == "Vẽ biểu đồ cột":
    plot_bar_chart()
elif task == "Vẽ biểu đồ đường":
    plot_line_chart()