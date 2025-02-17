from flask import Flask, jsonify
import cx_Oracle
#cx_Oracle.init_oracle_client(lib_dir=r"E:\streamlit\setup\instantclient_23_7")

app = Flask(__name__)

st.title('Dữ liệu từ Oracle qua API')
    
