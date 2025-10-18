import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def load_data():
    st.header("Tải Dữ Liệu Thuê Xe Đạp")
    day_data = None
    hour_data = None
    day_col, hour_col = st.columns(2)
    with day_col:
        day_file = st.file_uploader("Tải lên tệp CSV cho dữ liệu hàng ngày", type=["csv"])
        if day_file is not None:
            day_data = pd.read_csv(day_file)
            st.success("Tệp dữ liệu hàng ngày đã được tải lên thành công!")
        
    with hour_col:
        hour_file = st.file_uploader("Tải lên tệp CSV cho dữ liệu hàng giờ", type=["csv"])
        if hour_file is not None:
            st.success("Tệp dữ liệu hàng giờ đã được tải lên thành công!")
            hour_data = pd.read_csv(hour_file)
        
    if day_data is not None and hour_data is not None:
        st.success("Dữ liệu đã được tải thành công!")

    return day_data, hour_data

@st.cache_data
def load_day_csv(day_file):
    return pd.read_csv(day_file)

@st.cache_data
def load_hour_csv(hour_file):
    return pd.read_csv(hour_file)

def view_data(day_data, hour_data):
    st.header("Xem Dữ Liệu Thuê Xe Đạp")
    if day_data is not None:
        st.subheader("Dữ liệu thuê xe đạp hàng ngày")
        st.dataframe(day_data.head())
    else:
        st.warning("Dữ liệu hàng ngày chưa được tải lên.")
    
    if hour_data is not None:
        st.subheader("Dữ liệu thuê xe đạp hàng giờ")
        st.dataframe(hour_data.head())
    else:
        st.warning("Dữ liệu hàng giờ chưa được tải lên.")

def plot_correlation_matrix(day_data, hour_data):
    st.header("Ma trận tương quan của dữ liệu thuê xe đạp hàng ngày")
    if day_data is None or hour_data is None:
        st.warning("Vui lòng tải dữ liệu trước khi vẽ ma trận tương quan.")
        return

    dataset_choice = st.radio("Chọn bộ dữ liệu:", ("Ngày", "Giờ"), horizontal=True)
    data = day_data if dataset_choice == "Ngày" else hour_data
    select_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    selected_features = st.multiselect("Chọn đặc trưng", select_columns, default=select_columns[:5])

    fig, ax = plt.subplots(figsize=(10, 8))
    corr_matrix = data[selected_features].corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title(f"Ma trận tương quan - Dữ liệu {dataset_choice.lower()}")
    st.pyplot(fig)

def plot_bar_chart(day_data):
    st.header("Biểu đồ cột của dữ liệu thuê xe đạp hàng ngày")

    years = {0: '2011', 1: '2012'}
    selected_year = st.radio("Chọn năm:", years,
                             format_func=lambda x: years[x],
                             horizontal=True)
    data = day_data[day_data['yr'] == selected_year] # Lọc dữ liệu theo năm đã chọn

    season_mapping = {1: 'Mùa xuân', 2: 'Mùa hè', 3: 'Mùa thu', 4: 'Mùa đông'}
    season_data = data.groupby('season')['cnt'].sum().reindex()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(season_data.index.map(season_mapping), 
           season_data.values, 
           color=['#ff9999', '#ffcc99', '#99ff99', '#99ccff'])
    # sns.barplot(x=season_data.index.map(season_mapping), 
    #             y=season_data.values, 
    #             colors=['#ff9999', '#ffcc99', '#99ff99', '#99ccff'],
    #             ax=ax)
    ax.set_title(f"Số lượng thuê xe đạp theo mùa trong năm {years[selected_year]}")
    ax.set_xlabel("Mùa")
    ax.set_ylabel("Tổng số lượt thuê xe đạp")
    st.pyplot(fig)

def plot_line_chart(day_data):
    st.header("Biểu đồ đường của dữ liệu thuê xe đạp hàng giờ")

    years = {0: '2011', 1: '2012'}
    selected_year = st.radio("Chọn năm:", years,
                             format_func=lambda x: years[x],
                             horizontal=True)
    data = day_data[day_data['yr'] == selected_year] # Lọc dữ liệu theo năm đã chọn

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(data['dteday'], data['cnt'], marker='o', linestyle='-', color='b')
    ax.set_title(f"Số lượng thuê xe đạp hàng ngày trong năm {years[selected_year]}")
    ax.set_xlabel("Ngày")
    ax.set_ylabel("Số lượt thuê xe đạp")
    plt.xticks(rotation=45)
    st.pyplot(fig)

def predict_demand(day_data):
    st.header("Dự báo nhu cầu thuê xe đạp hàng ngày")

    test_ratio = st.slider("Tỉ lệ dữ liệu test (%)", min_value=10, max_value=50, value=20, step=5) / 100.0
    random_state = st.number_input("Random state", min_value=0, value=42, step=1, max_value=100)
    st.write("Tùy chỉnh siêu tham số: ")
    n_trees = st.slider("Số cây: ", 5, 100, 20, 5)
    max_depth = st.slider("Độ sâu tối đa: ", 1, 30, 5, 1)

    numeric_features = day_data.select_dtypes(include=[np.number]).columns.tolist()
    numeric_features.remove('cnt')  # Loại bỏ biến mục tiêu
    numeric_features.remove('instant')  # Loại bỏ biến không cần thiết
    

    X = day_data[numeric_features]
    y = day_data['cnt']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=random_state)

    # Tạo mô hình RF
    model = RandomForestRegressor(n_estimators=n_trees, max_depth=max_depth, random_state=random_state)
    # Huấn luyện mô hình
    model.fit(X_train, y_train)
    # Đánh giá mô hình
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    train_r2 = model.score(X_train, y_train)
    test_r2 = model.score(X_test, y_test)

    st.write("Đánh giá mô hình:")
    st.write(f"- MSE (Train): {train_mse:.2f}")
    st.write(f"- MSE (Test): {test_mse:.2f}")
    st.write(f"- R2 (Train): {train_r2:.2f}")
    st.write(f"- R2 (Test): {test_r2:.2f}")

    st.subheader("NGƯỜI DÙNG DỰ BÁO")

    input_data = {}
    for idx, col in enumerate(numeric_features):
        if col in ['temp', 'atemp', 'hum', 'windspeed']:
            input_data[col] = st.number_input(
                f'Cột {col}',
                min_value=float(X[col].min()),
                max_value=float(X[col].max()),
                value=float(X[col].mean()),
                format="%.2f"
            )
        else:
            input_data[col] = st.slider(
                f'Cột {col}',
                min_value=int(X[col].min()),
                max_value=int(X[col].max()),
                value=int(X[col].mean())
            )

    if st.button("Dự báo số lượt thuê xe đạp"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        st.success(f"Dự báo số lượt thuê xe đạp: {int(prediction[0])}")