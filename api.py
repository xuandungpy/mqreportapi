from flask import Flask, jsonify
import cx_Oracle

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    dsn_tns = cx_Oracle.makedsn('192.168.1.250', '1521', service_name='mqsoft')
    connection = cx_Oracle.connect(user='system', password='Mqsoft0989777722', dsn=dsn_tns)
    
    cursor = connection.cursor()
    cursor.execute('SELECT id, ma, ten, dang FROM mqsoftbvnhabe_test.d_dmbd')
       
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    
    data = [dict(zip(columns, row)) for row in rows]
    
    cursor.close()
    connection.close()
    
    response = jsonify(data)
    response.headers.add('Content-Type', 'application/json; charset=utf-8')
    return response

if __name__ == '__main__':
# app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
