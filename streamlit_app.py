import streamlit as st
import pandas as pd
import requests

# Gọi API để lấy dữ liệu
response = requests.get('http://127.0.0.1:5000/get-data')
data = response.json()

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Hiển thị dữ liệu bằng Streamlit
st.title('Dữ liệu từ Oracle qua API')
st.dataframe(df)